import React from 'react';

import { Button as GravityButton } from '@gravity-ui/uikit';

type ButtonProps = {
  label: string;
};


export const Button: React.FC<ButtonProps> = ({ label }) => (
  <GravityButton view={'normal'} loading={true}>{label}</GravityButton>
);