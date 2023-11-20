import Link from "next/link";

const LinkButton = ({ href, children, active }) => {
  return (
    <Link
      href={href}
      className={`p-2 text-center duration-300 grow rounded-md font-medium ${
        active
          ? "text-indigo-100 bg-indigo-700"
          : "hover:bg-indigo-700 hover:text-indigo-100"
      }`}
    >
      {children}
    </Link>
  );
};

export default LinkButton;
