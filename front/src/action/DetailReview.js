import React from "react";
import { randomValueFromArray } from "../action/HotelSearch";

const DetailReview = ({ reviews, positive }) => {
    return (
        <div>
            {reviews === undefined ? (
                <></>
            ) : (
                <div>
                    {reviews.map((review) => {
                        if (review.is_positive === positive)
                            return (
                                <React.Fragment key={review.review_id}>
                                    <div className="text-sm">
                                        <br />
                                    </div>
                                    <div className="card w-96 md:w-full bg-base-100 shadow-xl mb-1 cursor-default">
                                        <div className="card-body p-2 w-full">
                                            <h2 className="card-title items-end">
                                                <span>
                                                    @{randomValueFromArray()}
                                                    △△님,
                                                </span>
                                                <span className="text-sm ">
                                                    {review.review_date.slice(
                                                        0,
                                                        7
                                                    )}
                                                </span>
                                            </h2>
                                            <p className="p-3">
                                                {review.contents}
                                            </p>
                                        </div>
                                    </div>
                                </React.Fragment>
                            );
                        return (
                            <React.Fragment
                                key={review.review_id}
                            ></React.Fragment>
                        );
                    })}
                </div>
            )}
        </div>
    );
};

export default DetailReview;
