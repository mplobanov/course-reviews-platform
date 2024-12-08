import React from 'react';

import styles from './styles.module.css';
import { Course } from '../../../../types';
import { Button, Card, Text } from '@gravity-ui/uikit';
import { CourseMark } from '../course-mark/component';

interface Props {
  course: Course;
}

export const CourseMarks = ({ course: { marks } }: Props) => {
  return (
    <div className={styles.container}>
      <Text variant="subheader-3">Общая информация</Text>
      <Card>
        <div className={styles.marks}>
          {marks.map((mark, i) => (
            <CourseMark key={i} mark={mark} />
          ))}
          <Button width="max" size="l" view="action" style={{marginTop: '10px'}}>
            Добавить отзыв
          </Button>
        </div>
      </Card>
    </div>
  );
};
