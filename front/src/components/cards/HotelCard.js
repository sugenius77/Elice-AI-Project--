import React from "react";

const HotelCard = ({ h }) => {
    return (
        <>
            <div className="mb-3">
                <div className="bg-white grid rounded-2xl hover:scale-105 duration-150 text-fontcolor p-2 grid-cols-4">
                    <div className="text-blue">
                        <img
                            src="https://via.placeholder.com/900x500.png?text=Hotel+hoya"
                            alt="sample"
                            className="h-auto"
                        />
                    </div>
                    <div className="text-blue col-start-2 col-end-4 ml-2">
                        <div className="">
                            <h5>{h.title}</h5>
                            <h5>{h.review}</h5>
                        </div>
                    </div>
                </div>
            </div>
        </>
    );
};

export default HotelCard;
