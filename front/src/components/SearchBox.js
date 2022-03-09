import React, { useState, useEffect } from "react";
import { Links } from "./Link";
import { useDebounce } from "use-debounce";

import { useRecoilState, useRecoilValue } from "recoil";
import { testState, searchDataState } from "../state/atom";
import LocalBtn from "./LocalBtn";

const SearchBox = () => {
    // const [results, setResults] = useRecoilState(testState);
    // console.log("recoil 값은 ===>", results);
    const [searchData, setSearchData] = useRecoilState(searchDataState);

    const [text, setText] = useState("");
    const [selectLocal, setSelectLocal] = useState(["000"]); //TODO 000으로 수정필요

    const [search] = useDebounce(text, 500);
    const [region] = useDebounce(selectLocal, 300);

    useEffect(() => {
        if (search) setSearchData({ region, search });
        console.log(searchData);
    }, [search]);

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
                        className="sm:w-60  md:w-3/4  w-full h-10 dark:bg-gray-200 bg-gray-50  bg-none border-none rounded-full focus:outline-none p-6 focus:caret-point text-black flex mr-2 focus:scale-150 focus:mt-3 focus:ml-10 duration-100 focus:ring focus:ring-headerColor "
                        placeholder="🔎바다뷰가좋았어요 검색 "
                        onChange={(e) => setText(e.target.value)}
                    />

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
            </div>
        </div>
    );
};

export default SearchBox;
