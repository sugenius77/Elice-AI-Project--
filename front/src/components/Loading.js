import React from "react";
import ClimbingBoxLoader from "react-spinners/ClimbingBoxLoader";
import BounceLoader from "react-spinners/BounceLoader";

export const Loading = () => (
    <div className="flex justify-center items-center ">
        <ClimbingBoxLoader color="#fca311" size="15px" />
    </div>
);

export const Loading2 = () => (
    <div className="flex justify-center items-center my-5 ">
        <BounceLoader color="#F4A261" size="60px" />
    </div>
);
