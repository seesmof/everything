import Link from "next/link";

const LinkButton = ({ href, children, active }) => {
  return (
    <Link
      href={href}
      className={`p-2 duration-300 grow rounded-md ${
        active
          ? "text-white bg-slate-700"
          : "hover:bg-slate-700 hover:text-white"
      }`}
    >
      {children}
    </Link>
  );
};

export default LinkButton;
