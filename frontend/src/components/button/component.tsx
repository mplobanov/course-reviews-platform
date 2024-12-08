import React from 'react';

import { Button as GravityButton } from '@gravity-ui/uikit';

import styles from './button.module.css'

type ButtonProps = {
  label: string;
  onClick: () => void;
};


export const Button: React.FC<ButtonProps> = ({ label, onClick}) => (
  <GravityButton view={'normal'} className={styles.main} onClick={onClick}>{label}</GravityButton>
);