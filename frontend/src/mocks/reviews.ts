import { useMemo } from 'react';
import { Review } from '../types';

import umar from './assets/photo_2024-11-06_18-41-31.png';

const reviews: Review[] = [
  {
    author: {
      id: 1,
      name: 'Махсудов Умар Абдукахарович',
      profile_pic_url: umar,
      passport_token: 'abobus',
      is_superuser: false,
    },
    marks: [
      {
        id: 1,
        name: 'Сложность',
        value: 5,
        max_value: 5,
      },
      {
        id: 2,
        name: 'Организация',
        value: 2,
        max_value: 5,
      },
      {
        id: 3,
        name: 'Качество преподавания',
        value: 4,
        max_value: 5,
      },
      {
        id: 4,
        name: 'Полезность',
        value: 3,
        max_value: 5,
      },
      {
        id: 5,
        name: 'Общая оценка',
        value: 3,
        max_value: 5,
      },
    ],
    text: 'Надо выбрать небольшой проект или небольшой блок функциональности в большом проекте (например, пересылка фотографий в мессенджере или функциональность, позволяющая обмениваться стикерами, или добавление пароля для расшифровки архива в архиваторе и тп). Продумать с максимальной детализацией варианты использования, структуру классов и тонкости реализации.',
    is_extern: true,
    is_recredit: false,
    is_hidden: false,
    grades: [
      {
        type: 'like',
        count: 125,
      },
      {
        type: 'dislike',
        count: 125,
      },
    ],
  },
  {
    author: {
      id: 1,
      name: 'Махсудов Умар Абдукахарович',
      profile_pic_url: umar,
      passport_token: 'abobus',
      is_superuser: false,
    },
    marks: [
      {
        id: 1,
        name: 'Сложность',
        value: 5,
        max_value: 5,
      },
      {
        id: 2,
        name: 'Организация',
        value: 2,
        max_value: 5,
      },
      {
        id: 3,
        name: 'Качество преподавания',
        value: 4,
        max_value: 5,
      },
      {
        id: 4,
        name: 'Полезность',
        value: 3,
        max_value: 5,
      },
      {
        id: 5,
        name: 'Общая оценка',
        value: 3,
        max_value: 5,
      },
    ],
    text: 'Надо выбрать небольшой проект или небольшой блок функциональности в большом проекте (например, пересылка фотографий в мессенджере или функциональность, позволяющая обмениваться стикерами, или добавление пароля для расшифровки архива в архиваторе и тп). Продумать с максимальной детализацией варианты использования, структуру классов и тонкости реализации.',
    is_extern: true,
    is_recredit: false,
    is_hidden: true,
    grades: [
      {
        type: 'like',
        count: 12,
      },
      {
        type: 'dislike',
        count: 250,
      },
    ],
  },
];

// eslint-disable-next-line @typescript-eslint/no-unused-vars
export const useReviews = (_courseId: number) => useMemo(() => reviews, []);
