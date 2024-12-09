import React, { ReactNode } from 'react';

import styles from './styles.module.css';
import { Text } from '@gravity-ui/uikit';
import { Link } from 'react-router';

import profile_pic_url from '../../mocks/assets/photo_2024-11-06_18-41-31.png';

interface Props {
  children: ReactNode;
}

export const PageHead = ({ children }: Props) => {
  return (
    <div className={styles.container}>
      <div className={styles.head}>
        <Link to="/" className={styles.headLink}>
          <Text variant="display-1">Курсы 1С</Text>
        </Link>
        <div className={styles.spacer} />
        <img
          src={profile_pic_url}
          className={styles.profilePic}
          alt={'Аватарка'}
        />
      </div>
      <div className={styles.children}>{children}</div>
    </div>
  );
};
