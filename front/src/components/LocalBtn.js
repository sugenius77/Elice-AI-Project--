import React from "react";

const LocalBtn = ({ isProperty, setIsProperty }) => {
    console.log(isProperty);
    const handlePropertyBtn = (e) => {
        const { value } = e.target;
        if (value === "000") {
            setIsProperty(["000"]);
        } else if (isProperty.length === 5) {
            setIsProperty(["000"]);
        } else if (isProperty.find((e) => e === value)) {
            setIsProperty(isProperty.filter((e) => e !== value));
        } else if (isProperty.length > 0) {
            setIsProperty([...isProperty.filter((e) => e !== "000"), value]);
        } else {
            setIsProperty(["000"]);
        }
    };

    const location = ["전체", "서울", "제주", "부산", "강원", "여수"];
    const location2 = [
        { label: "전체", id: "000" },
        { label: "서울", id: "002" },
        { label: "제주", id: "064" },
        { label: "부산", id: "051" },
        { label: "강원", id: "033" },
        { label: "여수", id: "061" },
    ];

    return (
        <div className="flex md:justify-around justify-between items-center mb-3">
            {location2.map((local) => {
                return (
                    <>
                        <label
                            htmlFor={local.label}
                            className={` text-sm border rounded-2xl p-2 cursor-pointer shadow-sm ${
                                isProperty.includes(local.id) &&
                                "bg-point shadow text-white"
                            } `}
                        >
                            {local.label}
                        </label>
                        <input
                            type="button"
                            key={local.label}
                            value={local.id}
                            onClick={handlePropertyBtn}
                            id={local.label}
                            className="hidden"
                            // Clicked={isProperty.find((e) => e === { local })}
                        />
                    </>
                );
            })}
        </div>
    );
};

export default LocalBtn;

// import React from "react";

// const LocalBtn = ({ isProperty, setIsProperty }) => {
//     console.log(isProperty);
//     const handlePropertyBtn = (e) => {
//         const { value } = e.target;
//         if (value === "전체") {
//             setIsProperty(["전체"]);
//         } else if (isProperty.length === 5) {
//             setIsProperty(["전체"]);
//         } else if (isProperty.find((e) => e === value)) {
//             setIsProperty(isProperty.filter((e) => e !== value));
//         } else if (isProperty.length > 0) {
//             setIsProperty([...isProperty.filter((e) => e !== "전체"), value]);
//         } else {
//             setIsProperty(["전체"]);
//         }
//     };

//     const location = ["전체", "서울", "제주", "부산", "강원", "여수"];

//     return (
//         <div className="flex md:justify-around justify-between items-center mb-3">
//             {location.map((local) => {
//                 return (
//                     <input
//                         type="button"
//                         key={local}
//                         value={local}
//                         onClick={handlePropertyBtn}
//                         // Clicked={isProperty.find((e) => e === { local })}
//                         className={` text-sm border rounded-2xl p-2 cursor-pointer shadow-sm ${
//                             isProperty.includes(local) &&
//                             "bg-point shadow text-white"
//                         } `}
//                     />
//                 );
//             })}
//         </div>
//     );
// };

// export default LocalBtn;
