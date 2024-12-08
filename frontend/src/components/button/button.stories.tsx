import React from 'react';
import { Meta, StoryFn } from '@storybook/react';
import { Button } from './component';

import { ThemeProvider } from '@gravity-ui/uikit';

export default {
  title: 'Components/Button',
  component: Button,
} as Meta<typeof Button>;

const Template: StoryFn<{ label: string , onClick: () => void}> = (args) => (
  <ThemeProvider theme="light">
    <Button {...args} />
  </ThemeProvider>
);

export const Primary = Template.bind({});
Primary.args = {
  label: 'Click Me',
  onClick: () => console.log('Click Me'),
};
