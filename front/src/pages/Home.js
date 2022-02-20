import React, { useState } from "react";
import Layout from "components/Layout";

import SearchBox from "components/SearchBox";

const Home = () => {
    return (
        <Layout>
            <div className="min-h-screen w-full mt-10">
                <h1 className="text-4xl text-center m-5 font-semibold">
                    키보드로 소문난 호텔
                </h1>
                <SearchBox />
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
