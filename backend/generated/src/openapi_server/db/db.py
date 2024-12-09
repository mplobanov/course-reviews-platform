import sqlite3
import os


class DB:
    def __init__(self):
        self.dbPath = "/data.db"
        self.connection = sqlite3.connect(self.dbPath)

    def __del__(self):
        self.connection.close()

    def getCourses(self) -> list:
        result = []
        courses = self.connection.cursor().execute("SELECT Course.id, Teacher.id, Course.name, Course.externe, Teacher.surname, Teacher.name, Teacher.patronymic FROM Course LEFT JOIN Teacher on Course.teacher = Teacher.id").fetchall()
        for course in courses:
            course = list(course)
            courseRate = self.getCourseRate(course[0])
            teacherRate = self.getTeacherRate(course[1])
            course[3] = (course[3] != "Нет")
            result.append({"course": course,
                           "courseRate": courseRate,
                           "teacherRate": teacherRate})
        res = []
        for c in result:
            info = c['course']
            prerequisites = self.getPrerequisites(info[0])
            pr = []
            for p in prerequisites:
                pr.append({"id": p[0], "name": p[1]})
            res.append({
                'id': info[0],
                'name': info[2],
                'is_passed': False,
                'has_extern': info[3],
                'recredit_available': info[3],
                'teacher': {"id": info[0], "name": " ".join(info[4:]), "average_grade": c['teacherRate']},
                'prerequisites': pr,
                'avg_mark': c['courseRate']
            })

        return res

    def getTeacherRate(self, uid) -> float | None:
        query = "SELECT AVG(common_rate) FROM Review LEFT JOIN Course on Review.course_id = Course.id WHERE Course.teacher = ?"
        return self.connection.cursor().execute(query, (uid,)).fetchall()[0][0]

    def getCourseRate(self, uid) -> float:
        query = "SELECT AVG(common_rate) FROM Review LEFT JOIN Course on Review.course_id = Course.id WHERE Course.id = ?"
        return self.connection.cursor().execute(query, (uid,)).fetchall()[0][0]

    def getCourseInfo(self, uid):
        """
        Формат:
        {
            'common': [<course_id>, <teacher_id>, <Название>, <Описание>, <Экстерн>, <Перезачет>],
            'reviews': {<review_id>: [<Фамилия>, <Имя>, <Отчество>, <Текст>, <Сложность>, <Организация>, <Качество>, <Полезность>, <Общая оценка>, <дата>, <кол-во лайков>, <кол-во дизлайков>]}
            'prerequisites': [(<id курса>, <Название курса>)],
            'stat': {<course_id>: (Сложность>, <Организация>, <Качество>, <Полезность>, <Общая оценка>)}

            По поводу commonInfo - это средние оценки всех курсов сервиса, включая текущий

        }
        """
        return {'common': self.getCourseCommon(uid), 'reviews': self.getReviews(uid),
                'prerequisites': self.getPrerequisites(uid), 'stat': self.getAllCoursesStatistic()}

    def getCourseCommon(self, uid):
        infoQuery = "SELECT * FROM Course WHERE Course.id = ?"

        return list(self.connection.cursor().execute(infoQuery, (uid,)).fetchall()[0])

    def getTeacher(self, uid):
        query = """SELECT surname, Teacher.name, patronymic FROM Teacher
                LEFT JOIN Course on Course.teacher = Teacher.id
                WHERE Course.id = ?;
        """
        return " ".join(self.connection.cursor().execute(query, (uid,)).fetchall()[0]).strip()

    def getPrerequisites(self, uid):
        prerequisitesQuery = """SELECT prerequisite_id, Course.name FROM Prerequisite
                                    LEFT JOIN Course on prerequisite_id = Course.id
                                    WHERE course_id = ?
                                    """
        return self.connection.cursor().execute(prerequisitesQuery, (uid,)).fetchall()

    def getAllCoursesStatistic(self):
        statistics = {}

        infoQuery = """SELECT Course.id, AVG(difficulty), AVG(organization), AVG(quality), AVG(benefit), AVG(common_rate)  FROM Review
                            LEFT JOIN Course on Review.course_id = Course.id
                            GROUP BY Course.id
                            """

        res = self.connection.cursor().execute(infoQuery).fetchall()
        for r in res:
            statistics[r[0]] = r[1:]

        return statistics

    def getReviews(self, uid):
        reviews = {}
        reviewsQuery = """SELECT Review.id, User.surname, User.name, User.patronymic, txt, difficulty, quality, benefit, common_rate, date_time, Like.value FROM Review
                                LEFT JOIN Like on Like.review_id = Review.id
                                LEFT JOIN User on Review.user_id = User.id
                                WHERE Review.course_id = ?"""
        res = self.connection.cursor().execute(reviewsQuery, (uid,)).fetchall()
        for r in res:
            r = list(r)
            if r[0] not in reviews:
                reviews[r[0]] = r[1:-1] + [0, 0]

            if r[-1] == 1:
                reviews[r[0]][-2] += 1
            else:
                reviews[r[0]][-1] += 1

        return reviews
