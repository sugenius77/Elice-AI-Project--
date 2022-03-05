import React from "react";
import { randomValueFromArray } from "action/HotelSearch";

const DetailReview = ({ reviews, positive }) => {
    return (
        <div>
            {reviews === undefined ? (
                "null"
            ) : (
                <div>
                    {reviews.map((review, index) => {
                        if (review.is_positive === positive)
                            return (
                                <>
                                    <div
                                        key={review.review_id}
                                        className="text-sm"
                                    >
                                        <br />
                                    </div>
                                    <div className="card w-96 md:w-full bg-base-100 shadow-xl">
                                        <div clasNames="card-body">
                                            <h2 className="card-title">
                                                <span>
                                                    @{randomValueFromArray()}
                                                    △△님,
                                                </span>
                                                {review.review_date.slice(0, 7)}
                                            </h2>
                                            <p className="p-3">
                                                {review.contents}
                                            </p>
                                            <div className="card-actions justify-end"></div>
                                        </div>
                                    </div>
                                </>
                            );
                    })}
                </div>
            )}
        </div>
    );
};

export default DetailReview;
