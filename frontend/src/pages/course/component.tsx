import React, { ReactNode } from 'react';
import { Course } from '../../types';
import { PageHead } from '../../components/page-head/component';

import styles from './styles.module.css';
import { Description } from './ui/description/component';
import { CourseInfo } from './ui/course-info/component';
import { CourseMarks } from './ui/course-marks/component';

interface Props {
  course: Course;
  reviews: ReactNode;
}

export const CoursePageComponent = ({ course, reviews }: Props) => {
  return (
    <PageHead>
      <div className={styles.container}>
        <div className={styles.main}>
          <Description className={styles.titleAndDescription} course={course} />
          {reviews}
        </div>
        <div className={styles.cards}>
            <CourseInfo course={course} />
            <CourseMarks course={course} />
        </div>
      </div>
    </PageHead>
  );
};
