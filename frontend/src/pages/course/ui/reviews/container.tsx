import React from 'react';

import { useReviews } from "../../../../mocks/reviews";
import { ReviewsComponent } from "./component";

interface Props {
    courseId: number;
}

export const Reviews = ({ courseId }: Props) => {
    const reviews = useReviews(courseId);

    return <ReviewsComponent reviews={reviews} />;
};