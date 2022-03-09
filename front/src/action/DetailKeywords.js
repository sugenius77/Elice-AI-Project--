import React from "react";

const DetailKeywords = ({ data, positive }) => {
    let keywords = data.split("|");
    console.log("data", keywords);
    console.log(positive);

    return (
        <>
            {data !== undefined ? (
                <div className="mb-2">
                    {keywords.map((keyword) => (
                        <kbd
                            className={`kbd text-sm font-notoSans  ${
                                positive ? "border-blue-200" : "border-red-200"
                            }`}
                        >
                            {keyword}
                        </kbd>
                    ))}
                </div>
            ) : (
                ""
            )}
        </>
    );
};

export default DetailKeywords;
