import React from 'react';

import { Button as GravityButton } from '@gravity-ui/uikit';

import styles from './button.module.css'

type ButtonProps = {
  label: string;
};


export const Button: React.FC<ButtonProps> = ({ label }) => (
  <GravityButton view={'normal'} className={styles.main}>{label}</GravityButton>
);