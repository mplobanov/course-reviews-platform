import React from 'react';

import { useParams } from 'react-router';
import { useCourse } from '../../mocks/course';
import { CoursePageComponent } from './component';
import { Reviews } from './ui/reviews/container';

export const CoursePage = () => {
  const { id } = useParams();
  const courseId = Number.parseInt(id ?? '') ?? 1;
  const course = useCourse(courseId);

  return (
    <CoursePageComponent
      course={course}
      reviews={<Reviews courseId={courseId} />}
    />
  );
};
