import React, { useState } from "react";
import PropTypes from "prop-types";
import { Link, useHistory } from "react-router-dom";
import { Swiper, SwiperSlide } from "swiper/react";
import "swiper/css/pagination";
import "swiper/css/navigation";

import { Pagination } from "swiper";

import "swiper/css";
import HeartButton from "components/HeartButton";

const HotelCard = ({ h }) => {
    const history = useHistory();

    return (
        <>
            <div className="mb-3">
                <div className="bg-white grid rounded-2xl hover:scale-105 duration-150 text-fontcolor p-2 grid-cols-4 mx-4 md:flex-col md:flex ">
                    <div className="text-blue items-center ">
                        <img
                            src={h.hotel_img_url} //"https://via.placeholder.com/900x500.png?text=Hotel+hoya"
                            alt="sample"
                            className=" mr-3 rounded-lg w-96 h-60 mb-3 cursor-pointer"
                            onClick={() => history.push(`/hotel/${h.hotel_id}`)}
                        />
                    </div>
                    <div className="col-start-2  col-end-4 ml-2 ">
                        <div className="">
                            <Link
                                to={`/hotel/${h.hotel_id}`}
                                className="text-2xl font-bold hover:text-yellow-400 hover:shadow-sm"
                            >
                                {h.hotel_name}
                            </Link>
                            <span className="text-sm text-gray-400">
                                // {h.region}
                            </span>

                            {/* // Progress bar FIX 유사도 값 넣어야함 */}
                            <div className="mt-2">
                                <span></span>
                                <div className="w-full bg-gray-200 rounded-full">
                                    <div
                                        className="bg-point text-xs font-medium text-gray-500 text-center p-0.5 leading-none rounded-full"
                                        style={{ width: "45%" }}
                                    >
                                        Similarity : 45%
                                    </div>
                                </div>
                            </div>
                            <div className="h-40 w-full mt-1 ">
                                <Swiper
                                    direction={"vertical"}
                                    loop={true}
                                    pagination={{
                                        clickable: true,
                                    }}
                                    modules={[Pagination]}
                                    className="mySwiper w-full h-40 "
                                >
                                    {h.reviews.map((review) => (
                                        <SwiperSlide
                                            key={review.review_id}
                                            className=" pr-5 h-52 flex items-center justify-center"
                                        >
                                            <div>
                                                <p className="text-3xl inline-block">
                                                    “
                                                </p>{" "}
                                                <p className="text-center text-sm font-reviewsFont">
                                                    {review.contents}
                                                </p>{" "}
                                                <p className="text-sm text-center mt-3">
                                                    {review.review_date.slice(
                                                        0,
                                                        7
                                                    )}
                                                </p>
                                                <p className="text-3xl inline-block float-right pr-3">
                                                    ”
                                                </p>
                                            </div>
                                        </SwiperSlide>
                                    ))}
                                </Swiper>
                            </div>
                        </div>
                    </div>
                    <div className="flex w-full justify-center items-center md:mt-4">
                        <HeartButton />
                        <button
                            className="btn py-2 px-4 font-semibold items-center outline-none border-0  shadow-md text-white bg-[#5282a7] hover:bg-[#1c69a5] w-2/5 md:w-40"
                            onClick={() => window.open(h.hotel_url, "_blank")}
                        >
                            예약
                        </button>
                    </div>
                </div>
            </div>
        </>
    );
};

HotelCard.prototype = {
    h: PropTypes.array,
};

export default HotelCard;
