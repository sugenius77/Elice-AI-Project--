import React from "react";
import Layout from "components/Layout";
import Result from "components/Result";
import TestResult from "components/testResult";
import { Link } from "react-scroll";

import SearchBox from "components/SearchBox";

import AOS from "aos";

AOS.init({
    duration: 1000,
});

const Home = () => {
    return (
        <Layout id="1">
            <div className="min-h-screen bg-hero bg-cover">
                <div className="md:text-center items-center pt-24 pl-16 justify-center">
                    <h1 className="text-2xl md:text-xl pt-20 md:mt-0 mb-10 font-bold text-white text-doogle">
                        서비스 소개페이지
                    </h1>
                    <Link
                        to="2"
                        spy={true}
                        smooth={true}
                        className="py-2 px-4 font-semibold rounded-lg shadow-md text-white bg-blue-500 hover:bg-blue-700"
                    >
                        리뷰로 호텔찾기
                    </Link>
                </div>
            </div>
            <div>
                <div className=""></div>
                <div id="2" className=" w-full pt-20">
                    <h1 className="text-4xl text-center m-5 font-semibold text-fontcolor">
                        키보드로 소문난 호텔
                    </h1>
                    <h1 className="text-4xl text-center">⌨</h1>
                    <SearchBox />
                </div>
            </div>
            <div>
                <Result />
                {/* <TestResult></TestResult> */}
            </div>
        </Layout>
    );
};

export default Home;
