import React, { useState } from 'react';
import { Review as ReviewType } from '../../../../types';

import styles from './styles.module.css';
import { Text } from '@gravity-ui/uikit';
import { Detail } from './detail';
import { Grades } from '../grades/component';

interface Props {
  review: ReviewType;
}

export const Review = ({
  review: {
    author: { name, profile_pic_url },
    is_extern,
    is_recredit,
    is_hidden,
    marks,
    text,
    grades,
  },
}: Props) => {
  const [isHidden, setHidden] = useState(is_hidden);

  return (
    <div className={styles.container}>
      <div className={styles.author}>
        <img
          src={profile_pic_url}
          className={styles.profilePic}
          alt={'Аватарка'}
        />
        <Text variant="subheader-3">{name}</Text>
      </div>
      <div className={styles.facts}>
        {is_extern && <Detail text="Экстерн" />}
        {is_recredit && <Detail text="Перезачет" />}
        {marks.map(({ id, name, ...rest }) => (
          <Detail key={id} text={name} extra={rest} />
        ))}
      </div>
      {isHidden && <Text className={styles.hidden} variant='body-2' onClick={() => setHidden(false)}>Скрыто из-за низких оценок</Text>}
      {!isHidden && <Text variant="body-2">{text}</Text>}
      <Grades grades={grades} />
    </div>
  );
};
