import React, { useState, useEffect } from "react";
import { Links } from "./Link";
import { useDebounce } from "use-debounce";

import { useRecoilState, useRecoilValue } from "recoil";
import { testState, searchDataState } from "state/atom";
import LocalBtn from "./LocalBtn";

const SearchBox = () => {
    const [results, setResults] = useRecoilState(testState);
    console.log("recoil 값은 ===>", results);
    const [searchData, setSearchData] = useRecoilState(searchDataState);

    const [text, setText] = useState("hotels");
    const [selectLocal, setSelectLocal] = useState(["전체"]);

    const [inputValue] = useDebounce(text, 300);
    const [inputLocal] = useDebounce(selectLocal, 300);

    useEffect(() => {
        if (inputValue) setSearchData({ inputLocal, inputValue });
        console.log(searchData);
    }, [inputValue]);

    const filteredSearchValue = results.filter((result) => {
        return result.review.includes(text);
    }); //TODO API 데이터 들어오면 삭제 되어야함

    useEffect(() => {
        console.log(selectLocal);
    }, [selectLocal]);

    return (
        <div className="flex justify-center md:mx-5 mx-32 shadow-2xl bg-gray-50 items-center rounded-lg">
            <div className="py-10">
                <LocalBtn
                    isProperty={selectLocal}
                    setIsProperty={setSelectLocal}
                />
                <div className=" flex justify-center w-96 md:w-80 border rounded-full shadow-sm hover:shadow-lg">
                    <input
                        value={text}
                        type="text"
                        className="sm:w-60  md:w-3/4  w-full h-10 dark:bg-gray-200 bg-gray-50  bg-none border-none rounded-full outline-none p-6  focus:underline text-black  flex mr-2 "
                        placeholder="🔎 Search Hotel's Keyword in Reviews"
                        onChange={(e) => setText(e.target.value)}
                    />
                    <button type="submit"></button>
                    {text !== "" && (
                        <button
                            type="button"
                            className="flex text-2xl text-gray-500 items-center mx-3 "
                            onClick={() => setText("")}
                        >
                            x
                        </button>
                    )}
                </div>

                {/* <Links /> */}
                <hr className="mt-5" />

                {text.length > 2 ? (
                    <ul>
                        {filteredSearchValue.map((result) => {
                            return (
                                <div key={result._id}>
                                    {result.review} -{result.title}
                                </div>
                            );
                        })}
                    </ul>
                ) : (
                    ""
                )}
            </div>
        </div>
    );
};

export default SearchBox;
