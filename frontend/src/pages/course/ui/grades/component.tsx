import React from 'react';
import { useState } from 'react';
import { Grade } from '../../../../types';
import {
  ThumbsUpFill,
  ThumbsUp,
  ThumbsDownFill,
  ThumbsDown,
} from '@gravity-ui/icons';

import styles from './styles.module.css';
import { Text } from '@gravity-ui/uikit';

interface Props {
  grades: Grade[];
}

export const Grades = ({ grades }: Props) => {
  const [liked, setLiked] = useState<null | Grade['type']>(null);

  return (
    <div className={styles.container}>
      {grades.map(({ type, count }) => (
        <div
          key={type}
          className={styles.grade}
          onClick={() => setLiked((oldLiked) => (oldLiked === type ? null : type))}
        >
          {type === 'like' && liked === 'like' && <ThumbsUpFill />}
          {type === 'like' && liked !== 'like' && <ThumbsUp />}
          {type === 'dislike' && liked === 'dislike' && <ThumbsDownFill />}
          {type === 'dislike' && liked !== 'dislike' && <ThumbsDown />}
          <Text variant="body-1">{type === liked ? count + 1 : count}</Text>
        </div>
      ))}
    </div>
  );
};
