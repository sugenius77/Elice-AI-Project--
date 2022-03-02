import React from "react";

const LocalBtn = ({ isProperty, setIsProperty }) => {
    console.log(isProperty);
    const handlePropertyBtn = (e) => {
        const { value } = e.target;
        if (value === "전체") {
            setIsProperty(["전체"]);
        } else if (isProperty.length === 5) {
            setIsProperty(["전체"]);
        } else if (isProperty.find((e) => e === value)) {
            setIsProperty(isProperty.filter((e) => e !== value));
        } else if (isProperty.length > 0) {
            setIsProperty([...isProperty.filter((e) => e !== "전체"), value]);
        } else {
            setIsProperty(["전체"]);
        }
    };

    const location = ["전체", "서울", "제주", "부산", "강원", "여수"];

    return (
        <div className="flex md:justify-around justify-between items-center mb-3">
            {location.map((local) => {
                return (
                    <input
                        type="button"
                        key={local}
                        value={local}
                        onClick={handlePropertyBtn}
                        // Clicked={isProperty.find((e) => e === { local })}
                        className={` text-sm border rounded-2xl p-2 cursor-pointer shadow-sm ${
                            isProperty.includes(local) &&
                            "bg-point shadow text-white"
                        } `}
                    />
                );
            })}
        </div>
    );
};

export default LocalBtn;
