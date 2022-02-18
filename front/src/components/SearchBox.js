import React, { useState } from "react";
import { Links } from "./Link";

import { useRecoilState } from "recoil";
import { searchResultState } from "state/atom";

const SearchBox = () => {
    const [results, setResults] = useRecoilState(searchResultState);
    console.log("recoil 값은= =>>>", results);
    const [text, setText] = useState("hotels");

    // const [debouncedValue] = useDebounce(text, 300);

    const filterdSearchValue = results.filter((result) => {
        return result.includes(text);
    });

    return (
        <div className="flex justify-center md:mx-5 mx-32 shadow-2xl bg-gray-50 items-center rounded-lg">
            <div className="py-10">
                <div className=" flex justify-center w-96 border rounded-full  shadow-sm hover:shadow-lg">
                    <input
                        value={text}
                        type="text"
                        className="sm:w-96 w-full h-10 dark:bg-gray-200 bg-gray-50  bg-none border-none rounded-full outline-none p-6  focus:underline text-black  flex mr-2 "
                        placeholder="🔎 Search Google or type URL"
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

                <Links />

                {text.length > 2 ? (
                    <ul>
                        {filterdSearchValue.map((result) => {
                            return <li key={result}> {result} </li>;
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
