import React from "react";

const Progressbar = ({ value }) => {
    return (
        //  {/* // Progress bar FIX 유사도 값 넣어야함 */}
        <div className="mt-2">
            <div className="w-full bg-gray-200 rounded-full">
                <div
                    className="bg-sub text-xs font-medium text-gray-500 text-center p-0.5 leading-none rounded-full"
                    style={{ width: "45%" }}
                >
                    Similarity : 45%
                </div>
            </div>
        </div>
    );
};

export default Progressbar;
