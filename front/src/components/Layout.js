import React from "react";
import Footer from "./Footer";

const Layout = ({ children, id }) => {
  return (
    <div id={id}>
      <div className="content overflow-x-hidden font-notoSans bg-primary">
        {children}
      </div>
      <Footer />
    </div>
  );
};

export default Layout;
