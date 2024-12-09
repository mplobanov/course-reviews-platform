export type User = {
    id: number;
    name: string;
    profile_pic_url: string;
    passport_token: string;
    is_superuser: boolean;
}

export type Teacher = {
    id: number;
    name: string;
    average_grade: number;
}

export type Mark = {
    id: number;
    name: string;
    value: number;
    max_value: number;
}

export type Course = {
    id: number;
    name: string;

    teacher: Teacher;

    general_description: string;
    extern_description: string;
    recredit_desciption: string;

    extern_available: boolean;
    recredit_available: boolean;

    prerequisites: { id: number; name: string }[];

    marks: (Mark & { note?: { text: string; type: 'bad' | 'good' } })[];
}

export type Like = {
    type: 'like';
    count: number;
}

export type Dislike = {
    type: 'dislike',
    count: number;
}

export type Grade = Like | Dislike;

export type Review = {
    author: User;

    marks: Mark[];

    text: string;

    is_extern: boolean;
    is_recredit: boolean;

    is_hidden: boolean;

    grades: Grade[];
}

export type CourseFilter = {
    id: number;
    name: string;
}

export type GetCourseHandlerProps = {
    applied_filters_ids: number[];

    text_query: string;

    sort_by: 'default' | "teacher_grade_asc" | "teacher_grade_desc" | "course_grade_asc" | "course_grade_desc";

    prerequisite_ids: number[];

    cursor: string;
}

export type GetCourseHandler = (props: GetCourseHandlerProps) => { courses: Course[], next_page_cursor: string; prev_page_coursor: string };

export type GetCourse = (id: number) => Course;

interface GetCourseReviewsProps {
    course_id: string;
    cursor: string;
}

export type GetCourseReviews = (props: GetCourseReviewsProps) => { reviews: Review[]; next_cursor: string; };

export type PostReview = (review: Review) => void;

export type PostCourse = (course: Course) => void;

export type GetTeachers = (query: string) => Teacher[];