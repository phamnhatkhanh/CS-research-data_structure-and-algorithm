/*!

=========================================================
* Argon Dashboard React - v1.2.1
=========================================================

* Product Page: https://www.creative-tim.com/product/argon-dashboard-react
* Copyright 2021 Creative Tim (https://www.creative-tim.com)
* Licensed under MIT (https://github.com/creativetimofficial/argon-dashboard-react/blob/master/LICENSE.md)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/
// reactstrap components
import {
  Button,
  Card,
  CardHeader,
  CardBody,
  FormGroup,
  Form,
  Input,
  Container,
  Row,
  Col,
} from "reactstrap";
// core components

// import {fa-circle-info} from "@fortawesome/"
import HeaderCustom from "components/Headers/HeaderCustom";
import { useEffect, useState, Fragment } from "react";
import axios from "axios";

const StudyRecord = () => {
  const [chapter, setChapter] = useState([]);
  const [section, setSection] = useState([]);

  const handleSelectAll = (e) => {
    const { id, checked } = e.target;
    const id_chapter = id.split("customCheck")[1];

    setChapter(
      chapter.map((item) =>
        item.id == id_chapter ? { ...item, checked: checked } : item
      )
    );
    setSection(
      section.map((item) => {
        return item.id_chapter == id_chapter
          ? { ...item, checked: checked }
          : item;
      })
    );
  };

  // const setIschecked = (item, type) => {};

  const handleChange = (e) => {
    const { id, checked } = e.target;
    const id_section = id.split("Section")[1];
    setSection(
      section.map((item) =>
        item.id == id_section ? { ...item, checked: checked } : item
      )
    );
  };

  return (
    <>
      <HeaderCustom />
      <Card className="bg-secondary shadow  m-xl-4">
        <CardHeader className="bg-white border-0">
          <Row className="align-items-center">
            <Col className="text-left" xs="12">
              <h4>Accumulation score</h4>
            </Col>
          </Row>
        </CardHeader>
        <CardBody>
          <div className="pl-lg-4">
            <Row>
              <Col lg="12">
                <Row>
                  <Col
                    lg="6"
                    className="custom-control custom-radio mb-3"
                    id="custom-radio1"
                  >
                    <input
                      className="custom-control-input"
                      id="customRadio5"
                      name="radio-time"
                      type="radio"
                    />
                    <label
                      className="custom-control-label"
                      htmlFor="customRadio5"
                    >
                      Ứng dụng đạo hàm để khảo sát và vẽ đồ thị hàm số
                    </label>
                  </Col>
                  <Col lg="6">
                    <div className="progress-percentage">
                      <span>4.9 Score</span>
                    </div>
                    <div className="progress">
                      <div
                        className="progress-bar bg-info"
                        role="progressbar"
                        aria-valuenow="60"
                        aria-valuemin="0"
                        aria-valuemax="100"
                        style={{ width: "60%" }}
                      ></div>
                    </div>
                  </Col>
                </Row>
                <Row>
                  <Col
                    lg="6"
                    className="custom-control custom-radio mb-3"
                    id="custom-radio1"
                  >
                    <input
                      className="custom-control-input"
                      id="customRadio6"
                      name="radio-time"
                      type="radio"
                    />
                    <label
                      className="custom-control-label"
                      htmlFor="customRadio6"
                    >
                      Tính đơn điệu của hàm số
                    </label>
                  </Col>
                  <Col lg="6">
                    <div className="progress-percentage">
                      <span>4.9 Score</span>
                    </div>
                    <div className="progress">
                      <div
                        className="progress-bar bg-info"
                        role="progressbar"
                        aria-valuenow="60"
                        aria-valuemin="0"
                        aria-valuemax="100"
                        style={{ width: "60%" }}
                      ></div>
                    </div>
                  </Col>
                </Row>
                <Row>
                  <Col
                    lg="6"
                    className="custom-control custom-radio mb-3"
                    id="custom-radio1"
                  >
                    <input
                      className="custom-control-input"
                      id="customRadio7"
                      name="radio-time"
                      type="radio"
                    />
                    <label
                      className="custom-control-label"
                      htmlFor="customRadio7"
                    >
                      Giá trị lớn nhất - Giá trị nhỏ nhất của hàm số
                    </label>
                  </Col>
                  <Col lg="6">
                    <div className="progress-percentage">
                      <span>4.9 Score</span>
                    </div>
                    <div className="progress">
                      <div
                        className="progress-bar bg-info"
                        role="progressbar"
                        aria-valuenow="60"
                        aria-valuemin="0"
                        aria-valuemax="100"
                        style={{ width: "60%" }}
                      ></div>
                    </div>
                  </Col>
                </Row>
                <Row>
                  <Col
                    lg="6"
                    className="custom-control custom-radio mb-3"
                    id="custom-radio1"
                  >
                    <input
                      className="custom-control-input"
                      id="customRadio8"
                      name="radio-time"
                      type="radio"
                    />
                    <label
                      className="custom-control-label"
                      htmlFor="customRadio8"
                    >
                      Đường tiệm cận
                    </label>
                  </Col>
                  <Col lg="6">
                    <div className="progress-percentage">
                      <span>4.9 Score</span>
                    </div>
                    <div className="progress">
                      <div
                        className="progress-bar bg-info"
                        role="progressbar"
                        aria-valuenow="60"
                        aria-valuemin="0"
                        aria-valuemax="100"
                        style={{ width: "60%" }}
                      ></div>
                    </div>
                  </Col>
                </Row>
                <Row>
                  <Col
                    lg="6"
                    className="custom-control custom-radio mb-3"
                    id="custom-radio1"
                  >
                    <input
                      className="custom-control-input"
                      id="customRadio9"
                      name="radio-time"
                      type="radio"
                    />
                    <label
                      className="custom-control-label"
                      htmlFor="customRadio9"
                    >
                      Tương giao đồ thị
                    </label>
                  </Col>
                  <Col lg="6">
                    <div className="progress-percentage">
                      <span>4.9 Score</span>
                    </div>
                    <div className="progress">
                      <div
                        className="progress-bar bg-info"
                        role="progressbar"
                        aria-valuenow="60"
                        aria-valuemin="0"
                        aria-valuemax="100"
                        style={{ width: "60%" }}
                      ></div>
                    </div>
                  </Col>
                </Row>
                <Row>
                  <Col
                    lg="6"
                    className="custom-control custom-radio mb-3"
                    id="custom-radio1"
                  >
                    <input
                      className="custom-control-input"
                      id="customRadio10"
                      name="radio-time"
                      type="radio"
                    />
                    <label
                      className="custom-control-label"
                      htmlFor="customRadio10"
                    >
                      Tiếp tuyến của đồ thị hàm số
                    </label>
                  </Col>
                  <Col lg="6">
                    <div className="progress-percentage">
                      <span>4.9 Score</span>
                    </div>
                    <div className="progress">
                      <div
                        className="progress-bar bg-info"
                        role="progressbar"
                        aria-valuenow="60"
                        aria-valuemin="0"
                        aria-valuemax="100"
                        style={{ width: "60%" }}
                      ></div>
                    </div>
                  </Col>
                </Row>
                <Row>
                  <Col
                    lg="6"
                    className="custom-control custom-radio mb-3"
                    id="custom-radio1"
                  >
                    <input
                      className="custom-control-input"
                      id="customRadio11"
                      name="radio-time"
                      type="radio"
                    />
                    <label
                      className="custom-control-label"
                      htmlFor="customRadio11"
                    >
                      Sự biến thiên và đồ thị hàm số
                    </label>
                  </Col>
                  <Col lg="6">
                    <div className="progress-percentage">
                      <span>4.9 Score</span>
                    </div>
                    <div className="progress">
                      <div
                        className="progress-bar bg-info"
                        role="progressbar"
                        aria-valuenow="60"
                        aria-valuemin="0"
                        aria-valuemax="100"
                        style={{ width: "60%" }}
                      ></div>
                    </div>
                  </Col>
                </Row>
                <Row>
                  <Col
                    lg="6"
                    className="custom-control custom-radio mb-3"
                    id="custom-radio1"
                  >
                    <input
                      className="custom-control-input"
                      id="customRadio12"
                      name="radio-time"
                      type="radio"
                    />
                    <label
                      className="custom-control-label"
                      htmlFor="customRadio12"
                    >
                      Cực trị của hàm số
                    </label>
                  </Col>
                  <Col lg="6">
                    <div className="progress-percentage">
                      <span>4.9 Score</span>
                    </div>
                    <div className="progress">
                      <div
                        className="progress-bar bg-info"
                        role="progressbar"
                        aria-valuenow="60"
                        aria-valuemin="0"
                        aria-valuemax="100"
                        style={{ width: "60%" }}
                      ></div>
                    </div>
                  </Col>
                </Row>
              </Col>
            </Row>
            <Row></Row>
          </div>
        </CardBody>
      </Card>
      T T Phương Vi
      <Card className="bg-secondary shadow  m-xl-4">
        <CardHeader className="bg-white border-0">
          <Row>
            <Col className="text-left" xs="4">
              <h4>Exam details</h4>
            </Col>
            <Col className="text-right" xs="8">
              <Button className="align-self-end" color="info" type="submit">
                Review
              </Button>
              <Button className="align-self-end" color="info" type="submit">
                Practive
              </Button>
            </Col>
          </Row>
        </CardHeader>
        <CardBody>
          <Card>
            <Row>
              <Col xs="2">
                <text>ttphuongvi</text>
              </Col>
              <Col xs="2">
                <div>1.7</div>
                <text>Total right answer</text>
                <div>5/30</div>
              </Col>
              <Col xs="5">
                <span>Ứng dụng đạo hàm để khảo sát và vẽ đồ thị hàm số</span>
                <Row>
                  <Col xs="4">
                    <text>Grade</text>
                    <div>Grade 12</div>
                    <div>Duration</div>
                    <text>45m</text>
                  </Col>
                  <Col xs="4">
                    <text>Grade</text>
                    <div>Grade 12</div>
                    <div>Duration</div>
                    <text>45m</text>
                  </Col>
                  <Col xs="4">
                    <text>Grade</text>
                    <div>Grade 12</div>
                    <div>Duration</div>
                    <text>45m</text>
                  </Col>
                </Row>
              </Col>
            </Row>
          </Card>
        </CardBody>
      </Card>
    </>
  );
};

export default StudyRecord;
