import { useMemo } from 'react';
import { Course } from '../types';

const defaultCourse: Course = {
  id: 1,
  name: 'Архитектура 1',

  general_description:
    'Курс предполагает рассказ о базовых понятиях и принципах проектирования пользовательских интерфейсов: на что в первую очередь нужно обращать внимание, о каких моментах не стоит забывать и какую функциональность предоставлять в первую очередь. Курс планируется как несколько занятий, на которых вам расскажут основные принципы и покажут на живых примерах.',
  extern_description:
    'Надо выбрать небольшой проект или небольшой блок функциональности в большом проекте (например, пересылка фотографий в мессенджере или функциональность, позволяющая обмениваться стикерами, или добавление пароля для расшифровки архива в архиваторе и тп).  Продумать с максимальной детализацией варианты использования, структуру классов и тонкости реализации.',
  recredit_desciption: 'Нет',

  extern_available: true,
  recredit_available: false,

  teacher: {
    id: 1,
    name: 'Владимир Щелов',
    average_grade: 4.6,
  },

  prerequisites: [
    { id: 2, name: 'VCS' },
    { id: 3, name: 'Промышленное программирование' },
  ],

  marks: [
    {
      id: 1,
      name: 'Сложность',
      value: 2.5,
      max_value: 5,
    },
    {
      id: 2,
      name: 'Организация',
      value: 3,
      max_value: 5,
    },
    {
      id: 3,
      name: 'Качество преподавания',
      value: 5,
      max_value: 5,
      note: {
        text: 'Лучше обычного', 
        type: 'good',
      },
    },
    {
      id: 4,
      name: 'Полезность',
      value: 4,
      max_value: 5,
    },
    {
      id: 5,
      name: 'Общая оценка',
      value: 1,
      max_value: 5,
      note: {
        text: 'Хуже обычного', 
        type: 'bad',
      },
    },
  ],
};

// eslint-disable-next-line @typescript-eslint/no-unused-vars
export const useCourse = (_id: number) => useMemo(() => defaultCourse, []);
