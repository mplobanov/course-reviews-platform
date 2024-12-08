import React from 'react';
import { Text } from '@gravity-ui/uikit';
import { Review as ReviewType } from '../../../../types';

import styles from './styles.module.css';
import { Review } from '../review/component';

interface Props {
  reviews: ReviewType[];
}

export const ReviewsComponent = ({ reviews }: Props) => {
  return (
    <div className={styles.container}>
      <Text variant="display-1">Отзывы</Text>
      {reviews.map((review, id) => (
        <Review key={id} review={review} />
      ))}
    </div>
  );
};
