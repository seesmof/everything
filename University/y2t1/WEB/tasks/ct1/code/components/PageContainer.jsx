import React from "react";

const PageContainer = ({ className, children }) => {
  return (
    <div
      className={`${className} max-w-6xl mx-auto p-4 grid text-neutral-200 pb-20`}
    >
      {children}
    </div>
  );
};

export default PageContainer;
