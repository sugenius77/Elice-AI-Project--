import React from "react";
import PropTypes from "prop-types";
import { Link } from "react-router-dom";

const HotelCard = ({ h }) => {
    return (
        <>
            <div className="mb-3">
                <div className="bg-white grid rounded-2xl hover:scale-105 duration-150 text-fontcolor p-2 grid-cols-4 mx-4 md:flex-col md:flex ">
                    <div className="text-blue items-center ">
                        <img
                            src="https://via.placeholder.com/900x500.png?text=Hotel+hoya"
                            alt="sample"
                            className="h-auto"
                        />
                    </div>
                    <div className="col-start-2  col-end-4 ml-2">
                        <div className="">
                            <Link
                                to={`/hotel/${h._id}`}
                                className="text-2xl font-bold hover:text-gray-700"
                            >
                                {h.title}
                            </Link>
                            <h5>{h.review}</h5>
                        </div>
                    </div>
                    <div className="flex w-full justify-center items-center mt-4">
                        <button className="py-2 px-4 font-semibold rounded-lg shadow-md text-white bg-yellow-500 hover:bg-yellow-700 w-3/5 md:w-3/4">
                            바로가기
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
