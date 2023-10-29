export default function Loader() {
  return (
    <div className="d-flex flex-column justify-content-center">
      <div
        className="spinner-border align-self-center"
        role="status"
        style={{ width: "50px", height: "50px" }}
      >
        <span className="sr-only">Loading...</span>
      </div>
    </div>
  );
}
