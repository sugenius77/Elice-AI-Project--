import React from "react";

const About = () => {
    return (
        <>
            <div className="h-screen w-full mt-20 flex justify-center md:h-full md:my-36">
                <div className="w-[800px] mx-24 md:m-0 md:px-4 md:w-11/12  my-auto">
                    {/* <h1 className="text-6xl text-center m-5 font-title">
                        About
                    </h1> */}
                    <div className="flex flex-col w-full justify-between">
                        <h1 className="text-3xl text-[#374553] mb-3 font-title">
                            바다뷰가 너무 좋았어요
                            <span className="text-[#9DC3C2] text-6xl md:text-4xl">
                                .
                            </span>
                        </h1>
                        <p className="text-[#aaa] text-lg md:text-sm">
                            그 여행, 그 숙소에서 좋았던 경험을 검색해보세요!
                            <br />
                            이전의 경험을 바탕으로 잊지못할 호텔을 찾아주는
                            <br />
                            리뷰 기반 호텔 추천 서비스
                        </p>
                        <img
                            src="https://images.unsplash.com/photo-1440151050977-247552660a3b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1090&q=80"
                            alt="subtitle"
                            className="w-full my-5"
                        />
                    </div>
                </div>
            </div>
        </>
    );
};

export default About;
