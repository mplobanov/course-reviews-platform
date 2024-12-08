import React from 'react';

import styles from './styles.module.css';

interface Props {
  text: string;
  extra?: {
    value: number;
    max_value: number;
  };
}

export const Detail = ({ text, extra }: Props) => {
  if (!extra) {
    return <div className={`${styles.fact} ${styles.neutralFact}`}>{text}</div>;
  }

  const { value, max_value } = extra;

  if (value / max_value < 0.5) {
    return (
      <div className={`${styles.fact} ${styles.badFact}`}>
        {text}
        {': '}
        {value}
      </div>
    );
  }

  if (value / max_value > 0.85) {
    return (
      <div className={`${styles.fact} ${styles.goodFact}`}>
        {text}
        {': '}
        {value}
      </div>
    );
  }

  return (
    <div className={`${styles.fact} ${styles.neutralFact}`}>
      {text}
      {': '}
      {value}
    </div>
  );
};
