users = [
    {"id": 0, "name": "Umar Makhsudov",
        "passport_token": "null", "is_superuser": True},
    {"id": 1, "name": "Elena Petrova",
        "passport_token": "token123", "is_superuser": False},
    {"id": 2, "name": "Dmitry Ivanov",
        "passport_token": "token456", "is_superuser": True},
    {"id": 3, "name": "Anna Smirnova",
        "passport_token": "token789", "is_superuser": False},
    {"id": 4, "name": "Maxim Kozlov",
        "passport_token": "token012", "is_superuser": True},
    {"id": 5, "name": "Olga Sokolova",
        "passport_token": "token345", "is_superuser": False},
    {"id": 6, "name": "Ivan Lebedev",
        "passport_token": "token678", "is_superuser": True},
    {"id": 7, "name": "Svetlana Orlova",
        "passport_token": "token901", "is_superuser": False},
    {"id": 8, "name": "Artem Kravtsov",
        "passport_token": "token234", "is_superuser": True},
    {"id": 9, "name": "Natalia Vinogradova",
        "passport_token": "token567", "is_superuser": False}
]


teachers = [
    {"id": 1, "name": "Vladimir Shchelov", "average_grade": 4.6},
    {"id": 2, "name": "Irina Volkova", "average_grade": 4.8},
    {"id": 3, "name": "Alexey Morozov", "average_grade": 4.2},
    {"id": 4, "name": "Tatiana Karpova", "average_grade": 4.7},
    {"id": 5, "name": "Sergey Chernov", "average_grade": 4.5},
    {"id": 6, "name": "Yulia Belova", "average_grade": 4.9},
    {"id": 7, "name": "Oleg Zhukov", "average_grade": 4.3},
    {"id": 8, "name": "Maria Kuznetsova", "average_grade": 4.6},
    {"id": 9, "name": "Dmitry Fedorov", "average_grade": 4.4},
    {"id": 10, "name": "Sofia Popova", "average_grade": 4.8}
]

marks = [
    {"id": 0, "name": "Complexity", "value": 5.5, "max_value": 10.0},
    {"id": 1, "name": "Engagement", "value": 8.0, "max_value": 10.0},
    {"id": 2, "name": "Difficulty", "value": 6.5, "max_value": 10.0},
    {"id": 3, "name": "Clarity", "value": 7.0, "max_value": 10.0},
    {"id": 4, "name": "Structure", "value": 9.0, "max_value": 10.0},
    {"id": 5, "name": "Practicality", "value": 7.5, "max_value": 10.0},
    {"id": 6, "name": "Relevance", "value": 8.5, "max_value": 10.0},
    {"id": 7, "name": "Interaction", "value": 6.0, "max_value": 10.0},
    {"id": 8, "name": "Feedback", "value": 7.8, "max_value": 10.0},
    {"id": 9, "name": "Overall Impression", "value": 9.5, "max_value": 10.0}
]


courses_short_info = [
    {
        "id": 1,
        "name": "Arch1",
        "is_passed": True,
        "has_extern": False,
        "recredit_available": False,
        "teacher": teachers[0],
        "marks": marks[0:2],
        "prerequisites": [{"id": 0, "name": "VCS"}]
    },
    {
        "id": 2,
        "name": "Data Structures",
        "is_passed": False,
        "has_extern": True,
        "recredit_available": True,
        "teacher": teachers[1],
        "marks": marks[2:5],
        "prerequisites": [{"id": 1, "name": "Algorithms"}]
    },
    {
        "id": 3,
        "name": "Databases",
        "is_passed": True,
        "has_extern": False,
        "recredit_available": False,
        "teacher": teachers[3],
        "marks": marks[3:7],
        "prerequisites": [{"id": 2, "name": "SQL Basics"}]
    }
]

cources_info = [
    {
        **courses_short_info[0],
        "general_description": "An introductory course on system architecture",
    },
    {
        **courses_short_info[1],
        "general_description": "Advanced data management concepts are covered in this course.",
        "extern_description": "Students can complete this course externally by submitting a portfolio of practical assignments.",
        "recredit_description": "Recrediting is possible upon demonstration of equivalent prior learning."
    },
    {
        **courses_short_info[2],
        "general_description": "Comprehensive overview of database systems"
    }
]


reviews = [
    {
        "author": users[0],
        "marks": marks[0:5],
        "text": "Course content was very clear and informative.",
        "is_extern": False,
        "is_recredit": False,
        "is_hidden": False,
        "grades": {"likes": 10, "dislikes": 2}
    },
    {
        "author": users[1],
        "marks": marks[0:5],
        "text": "The teacher's approach was engaging and helpful.",
        "is_extern": True,
        "is_recredit": True,
        "is_hidden": False,
        "grades": {"likes": 15, "dislikes": 1}
    },
    {
        "author": users[2],
        "marks": marks[0:5],
        "text": "The material was moderately difficult but manageable.",
        "is_extern": False,
        "is_recredit": True,
        "is_hidden": False,
        "grades": {"likes": 8, "dislikes": 3}
    },
    {
        "author": users[3],
        "marks": marks[0:5],
        "text": "The explanations provided lacked clarity in some sections.",
        "is_extern": False,
        "is_recredit": False,
        "is_hidden": False,
        "grades": {"likes": 5, "dislikes": 6}
    },
    {
        "author": users[4],
        "marks": marks[0:5],
        "text": "The structure of the course content was well-organized.",
        "is_extern": True,
        "is_recredit": False,
        "is_hidden": False,
        "grades": {"likes": 20, "dislikes": 0}
    },
    {
        "author": users[5],
        "marks": marks[0:5],
        "text": "Practical examples made the material easier to understand.",
        "is_extern": False,
        "is_recredit": True,
        "is_hidden": False,
        "grades": {"likes": 10, "dislikes": 4}
    },
    {
        "author": users[6],
        "marks": marks[0:5],
        "text": "The course content was very relevant to current trends.",
        "is_extern": True,
        "is_recredit": False,
        "is_hidden": False,
        "grades": {"likes": 12, "dislikes": 1}
    },
    {
        "author": users[7],
        "marks": marks[0:5],
        "text": "Interaction between students and instructors could be improved.",
        "is_extern": False,
        "is_recredit": False,
        "is_hidden": False,
        "grades": {"likes": 3, "dislikes": 8}
    },
    {
        "author": users[8],
        "marks": marks[0:5],
        "text": "Feedback was timely and helpful for improving performance.",
        "is_extern": True,
        "is_recredit": True,
        "is_hidden": False,
        "grades": {"likes": 18, "dislikes": 2}
    },
    {
        "author": users[9],
        "marks": marks[0:5],
        "text": "Overall, this was one of the most informative courses I have taken.",
        "is_extern": False,
        "is_recredit": True,
        "is_hidden": False,
        "grades": {"likes": 25, "dislikes": 3}
    }
]

courses_reviews = dict()

for course in cources_info:
    cid = course["id"]
    begin = (cid - 1) * 3
    end = begin + 3
    rev = reviews[begin:end]
    courses_reviews[cid] = rev
