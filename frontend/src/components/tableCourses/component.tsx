import React from 'react';
import {
  Table as GravityTable,
  withTableSorting,
  withTableActions,
  Checkbox,
  Label,
  Text,
} from '@gravity-ui/uikit';
import styles from './component.module.css';
import { coursesVar } from '../../pages/mainPage/mainPage';
import { useReactiveVar } from '@apollo/client';
import teachers from '../../data/teachers.json';
import { Link } from 'react-router';

export const Table = () => {
  const MyTable = withTableSorting(withTableActions(GravityTable));
  const courses = useReactiveVar(coursesVar);

  const changePassedCourse = (id: number) => {
    const newCourses = courses.slice(0);
    newCourses[id].passed = !courses[id].passed;
    coursesVar(newCourses);
  };

  const searchTeacherAssessement = (teacherName: string) => {
    const teacherCurrent = teachers.filter(
      (item) => item.teacher === teacherName,
    );
    return teacherCurrent[0].assessment;
  };

  const dataCoursesConversion = () => {
    const coursesNow: {
      id: number;
      nameCourse: JSX.Element;
      passed: JSX.Element;
      extern: JSX.Element;
      lightness: number;
      teacher: JSX.Element;
      generalAssessment: number;
    }[] = courses.map((it, id) => {
      return {
        id: it.id,
        nameCourse: <Link to="/course/1">{it.nameCourse}</Link>,
        passed: (
          <div>
            <Checkbox
              checked={it.passed}
              onChange={() => changePassedCourse(id)}
              className={styles.passed}
              size="l"
            />
          </div>
        ),
        extern: (
          <div>
            <Text
              color={it.extern ? 'positive' : 'danger'}
              className={styles.extern}
            >
              {it.extern ? 'Да' : 'Нет'}
            </Text>
          </div>
        ),
        lightness: it.lightness,
        teacher: (
          <div>
            <span style={{marginRight: '10px'}}>{it.teacher}</span>
            <Label theme={'normal'}>
              {searchTeacherAssessement(it.teacher)}
            </Label>
          </div>
        ),
        generalAssessment: it.generalAssessment,
      };
    });
    return coursesNow;
  };

  const columns = [
    { id: 'id', name: 'id', className: styles.cellId },
    {
      id: 'nameCourse',
      name: 'Название курса',
      className: styles.cellNameCourse,
    },
    { id: 'passed', name: 'Пройден', className: styles.Passed },
    { id: 'extern', name: 'Экстрен', className: styles.Extern },
    {
      id: 'teacher',
      name: 'Преподаватель',
      meta: { sort: true },
      className: styles.cellTeacher,
    },
    {
      id: 'generalAssessment',
      name: 'Общая оценка',
      meta: { sort: true },
      className: styles.cellAssessment,
    },
  ];

  return (
    <MyTable
      data={dataCoursesConversion()}
      columns={columns}
      className={styles.main}
    />
  );
};
