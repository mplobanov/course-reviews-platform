import React from 'react';

import styles from './styles.module.css';
import { Mark } from '../../../../types';
import { Text } from '@gravity-ui/uikit';

interface Props {
  mark: Mark & { note?: { text: string; type: 'bad' | 'good' } };
}

export const CourseMark = ({
  mark: { name, max_value, value, note },
}: Props) => {
  return (
    <div className={styles.container}>
      <div className={styles.caption}>
        <Text variant="caption-2">{name}</Text>
        {note && (
          <>
            <span className={styles.spacer} />
            <Text
              variant="caption-2"
              color={note.type === 'good' ? 'positive-heavy' : 'danger-heavy'}
            >
              {note.text}
            </Text>
          </>
        )}
      </div>

      <div className={styles.barContainer}>
        <div className={styles.bar}>
          <div className={styles.backBar}></div>
          <div
            className={styles.valueBar}
            style={{ width: `${(value / max_value) * 100}%` }}
          ></div>
        </div>
        <Text variant="caption-2" className={styles.value}>
          {value}
        </Text>
      </div>
    </div>
  );
};
