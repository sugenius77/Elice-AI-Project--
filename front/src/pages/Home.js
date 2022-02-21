import React from "react";
import Layout from "components/Layout";
import Result from "components/Result";

import SearchBox from "components/SearchBox";

const Home = () => {
    return (
        <Layout>
            <div className=" w-full mt-24">
                <h1 className="text-4xl text-center m-5 font-semibold text-fontcolor">
                    키보드로 소문난 호텔
                </h1>
                <h1 className="text-4xl text-center">⌨</h1>
                <SearchBox />
            </div>
            <div>
                <Result />
            </div>
            <div id="1" className="">
                <div className=" mx-20 items-center mt-20">
                    <h1 className="text-2xl md:text-xl mt-5 md:mt-0">
                        Hello world
                        <b className="text-red-400">Developer</b>
                    </h1>
                </div>
            </div>
        </Layout>
    );
};

export default Home;
