import React from 'react';
import { Course } from '../../../../types';

import styles from './styles.module.css';
import { Text } from '@gravity-ui/uikit';

interface Props {
  className: string;
  course: Course;
}

export const Description = ({
  className,
  course: {
    name,
    general_description,
    extern_description,
    recredit_desciption,
  },
}: Props) => (
  <div className={className}>
    <Text variant="display-1">{name}</Text>
    <div className={styles.description}>
      <div className={styles.descriptionSection}>
        <Text variant="header-1">Описание курса</Text>
        <Text variant="body-2">{general_description}</Text>
      </div>
    </div>
    <div className={styles.description}>
      <div className={styles.descriptionSection}>
        <Text variant="header-1">Экстерн</Text>
        <Text variant="body-2">{extern_description}</Text>
      </div>
    </div>
    <div className={styles.description}>
      <div className={styles.descriptionSection}>
        <Text variant="header-1">Перезачет</Text>
        <Text variant="body-2">{recredit_desciption}</Text>
      </div>
    </div>
  </div>
);
