import React from "react";
import PropTypes from "prop-types";
import { Link } from "react-router-dom";
import { Swiper, SwiperSlide } from "swiper/react";
import "swiper/css/pagination";
import "swiper/css/navigation";

import { Autoplay, Pagination, Navigation } from "swiper";

import "swiper/css";

const HotelCard = ({ h }) => {
    return (
        <>
            <div className="mb-3">
                <div className="bg-white grid rounded-2xl hover:scale-105 duration-150 text-fontcolor p-2 grid-cols-4 mx-4 md:flex-col md:flex ">
                    <div className="text-blue items-center ">
                        <img
                            src={h.hotel_img_url} //"https://via.placeholder.com/900x500.png?text=Hotel+hoya"
                            alt="sample"
                            className=" mr-3 rounded-lg w-96 h-60 mb-3"
                        />
                    </div>
                    <div className="col-start-2  col-end-4 ml-2 ">
                        <div className="">
                            <Link
                                to={`/hotel/${h.hotel_id}`}
                                className="text-2xl font-bold hover:text-gray-700"
                            >
                                {h.hotel_name}
                            </Link>
                            <span className="text-sm text-gray-400">
                                // {h.region}
                            </span>
                            <div className="h-52 w-full mt-3">
                                <Swiper
                                    direction={"vertical"}
                                    loop={true}
                                    pagination={{
                                        clickable: true,
                                    }}
                                    // navigation={true}
                                    modules={[Navigation, Pagination]}
                                    className="mySwiper w-full h-40"
                                >
                                    {h.reviews.map((review) => (
                                        <SwiperSlide
                                            key={review.hotel_id}
                                            className=" pr-5 h-52"
                                        >
                                            <p className="text-3xl inline-block">
                                                “
                                            </p>{" "}
                                            <p className="text-center text-sm font-reviewsFont">
                                                {review[0]
                                                    ? review[0].contents
                                                    : ""}
                                            </p>{" "}
                                            <p className="text-3xl inline-block float-right pr-3">
                                                ”
                                            </p>
                                        </SwiperSlide>
                                    ))}
                                </Swiper>
                            </div>
                        </div>
                    </div>
                    <div className="flex w-full justify-center items-center mt-4">
                        <a
                            href={h.hotel_url}
                            target="_blank"
                            rel="noopener noreferrer"
                            className="w-40"
                        >
                            <button className="py-2 px-4 font-semibold rounded-lg shadow-md text-white bg-yellow-500 hover:bg-yellow-700 w-40 md:w-40">
                                예약
                            </button>
                        </a>
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
