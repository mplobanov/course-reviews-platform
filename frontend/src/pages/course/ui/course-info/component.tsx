import React from 'react';
import { Course } from '../../../../types';
import styles from './styles.module.css';
import { Card, Label, Text } from '@gravity-ui/uikit';
import { Link } from 'react-router';

interface Props {
  course: Course;
}

export const CourseInfo = ({
  course: {
    teacher: { name, average_grade },
    recredit_available,
    extern_available,
    prerequisites,
  },
}: Props) => {
  return (
    <div className={styles.container}>
      <Text variant="subheader-3">Общая информация</Text>
      <Card>
        <div className={styles.details}>
          <div className={styles.detail}>
            <Text variant="caption-2" className={styles.label}>
              Преподаватель
            </Text>
            <span className={styles.teacher}>
              <Text variant="body-1">{name}</Text>
              <Label>{average_grade}</Label>
            </span>
          </div>
          <div className={styles.detail}>
            <Text variant="caption-2" className={styles.label}>
              Перезачет
            </Text>
            <div className={styles.value}>
              <Label theme={recredit_available ? 'success' : 'danger'}>
                {recredit_available ? 'Да' : 'Нет'}
              </Label>
            </div>
          </div>
          <div className={styles.detail}>
            <Text variant="caption-2" className={styles.label}>
              Экстерн
            </Text>
            <div className={styles.value}>
              <Label theme={extern_available ? 'success' : 'danger'}>
                {extern_available ? 'Да' : 'Нет'}
              </Label>
            </div>
          </div>
          <div className={styles.detail}>
            <Text variant="caption-2" className={styles.label}>
              Пререквизиты
            </Text>
            <span className={styles.requisites}>
              {prerequisites.map(({ name, id }) => (
                <Link key={id} to={`/course/${id}`}>
                  <Text color="brand">{name}</Text>
                </Link>
              ))}
            </span>
          </div>
        </div>
      </Card>
    </div>
  );
};
