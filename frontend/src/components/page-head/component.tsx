import React, { ReactNode } from 'react';

import styles from './styles.module.css';
import { Text } from '@gravity-ui/uikit';
import { Link } from 'react-router';

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
      </div>
      <div className={styles.children}>{children}</div>
    </div>
  );
};
