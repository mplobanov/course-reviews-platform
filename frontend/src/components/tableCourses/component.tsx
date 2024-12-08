import {Table as GravityTable, withTableSorting, withTableActions, Checkbox, Label, Text} from '@gravity-ui/uikit';
import styles from './component.module.css'
import { coursesVar } from '../../pages/mainPage/mainPage';
import { useReactiveVar } from '@apollo/client';
import teachers from '../../data/teachers.json'
import { storeValueIsStoreObject } from '@apollo/client/cache/inmemory/helpers';



export const Table = () => {
    const MyTable = withTableSorting(withTableActions(GravityTable));
    let courses = useReactiveVar(coursesVar)

    const changePassedCourse = (id: number) => {
        const newCourses = courses.slice(0)
        newCourses[id].passed = !courses[id].passed
        coursesVar(newCourses)
    }

    const searchTeacherAssessement = (teacherName: string) => {
        const teacherCurrent = teachers.filter((item) => item.teacher === teacherName)
        return teacherCurrent[0].assessment
    }

    const dataCoursesConversion = () => {
        const coursesNow: {
            id: number;
            nameCourse: string;
            passed: JSX.Element;
            extern: JSX.Element;
            lightness: number;
            teacher: JSX.Element;
            generalAssessment: number;
        }[] = []
        courses.map((it, id) => {
            coursesNow.push({
                "id": it.id,
                "nameCourse": it.nameCourse,
                "passed": <div>
                            <Checkbox checked={it.passed} onChange={() => changePassedCourse(id)} className={styles.passed} size='l'/>
                        </div>,
                "extern": <div>
                            <Text color={it.extern ? "positive" : "danger"} className={styles.extern}>{it.extern ? "Да" : "Нет"}</Text>
                        </div>,
                "lightness": it.lightness,
                "teacher": <div>
                                {it.teacher}
                                <Label theme={"normal"}>{searchTeacherAssessement(it.teacher)}</Label>
                            </div>,
                "generalAssessment": it.generalAssessment
            })
        })
        return coursesNow
    }
    

    const columns =     [{id: 'id', name:'id', className: styles.cellId},
                         {id: 'nameCourse', name:'название курса', className: styles.cellNameCourse},
                         {id: 'passed', name:'пройден', className: styles.Passed},
                         {id: 'extern', name:'экстрен', className: styles.Extern},
                         {id: 'teacher', name:'преподаватель', meta: {sort: true}, className: styles.cellTeacher},
                         {id: 'generalAssessment', name:'общая оценка', meta: {sort: true}, className: styles.cellAssessment}]

    return (
        <MyTable data={dataCoursesConversion()} columns={columns} className={styles.main}/>
    )
}
    
  

