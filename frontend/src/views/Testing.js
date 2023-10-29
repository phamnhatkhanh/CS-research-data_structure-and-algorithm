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
  Modal,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Nav,
  NavLink,
  NavItem,
  TabContent,
  TabPane,
} from "reactstrap";
import classnames from "classnames";
// core components
import HeaderCustom from "components/Headers/HeaderCustom";
import { useEffect, useState, Fragment } from "react";
import { useDispatch, useSelector } from "react-redux";
import axios from "axios";
import { createNewTest } from "redux/action/test.action";
import Loader from "components/Loader";
import { CircularProgressbar } from "react-circular-progressbar";
import "react-circular-progressbar/dist/styles.css";

const RawHTML = ({ children, className = "" }) => (
  <div
    className={className}
    dangerouslySetInnerHTML={{ __html: children.replace(/\n/g, "<br />") }}
  />
);

const Testing = () => {
  const currentUser = JSON.parse(localStorage.getItem("currentUser"));
  const [chapter, setChapter] = useState([]);
  const [section, setSection] = useState([]);
  const dispatch = useDispatch();
  const testreducer = useSelector((state) => state.createTestReducer);
  const { loading, error, success, question, test, hasquestion } = testreducer;
  const [timeRemain, setTimeRemain] = useState(0);
  const [maxTime, setMaxTime] = useState(0);
  const [tab, setTab] = useState(1);
  const toggleNavs = (e, state, index) => {
    e.preventDefault();
    setTab(index);
  };

  let deadline;

  useEffect(() => {
    console.log(question);
  }, [question]);

  useEffect(() => {
    if (test) {
      setMaxTime(test.time * 60);
      setTimeRemain(test.time * 60);
      deadline = new Date(Date.parse(new Date()) + (test.time * 60 + 1) * 1000);
      console.log(deadline);

      const interval = setInterval(() => {
        setTimeRemain((deadline - new Date()) / 1000);
      }, 1000);
    }
  }, [test]);

  useEffect(() => {
    axios
      .get("/chapter/section")
      .then((res) => {
        if (res.data) {
          console.log(res.data);
          res.data.chapter = res.data.chapter.map((item) => {
            return { ...item, checked: false };
          });
          setChapter(res.data.chapter);

          res.data.section = res.data.section.map((item) => {
            return { ...item, checked: false };
          });
          // res.data.section.map((item) => { ...item, "checked": false});
          setSection(res.data.section);
        }
      })
      .catch((err) => {});
  }, []);

  const handleSubmitFormTest = (e) => {
    e.preventDefault();
    let list_answer = [];
    question.map((item) => {
      list_answer.push({
        id: item.Question.id,
        answer: e.target["question-radio-" + item.Question.id].value,
      });
    });

    const test_payload = {
      list_answer: list_answer,
    };
    axios
      .post("/tests/" + test.id, test_payload)
      .then((res) => {
        if (res.data) {
          console.log(res.data);
          alert(res.data.score);
        }
      })
      .catch((err) => {});
  };

  const handleSubmitForm = (e) => {
    e.preventDefault();

    let list_section = [];
    section.map((item) => {
      if (item.checked) {
        list_section.push(item.id);
      }
    });

    dispatch(
      createNewTest({
        list_id: list_section,
        time: e.target["radio-time"].value,
        id_user: currentUser.id,
      })
    );
  };

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

  const listChapter = chapter.map((item, index) => (
    <Fragment key={index}>
      <div key={item.id} className="custom-control custom-checkbox mb-2">
        <input
          className="custom-control-input"
          id={"customCheck" + item.id}
          type="checkbox"
          checked={item.checked}
          onChange={handleSelectAll}
        />
        <label
          className="custom-control-label"
          htmlFor={"customCheck" + item.id}
        >
          {item.name}
        </label>
      </div>
      {section.map((item2, index2) => (
        <Fragment key={index * 100 + index2}>
          {item2.id_chapter === item.id && (
            <div className="custom-control custom-checkbox mb-2 ml-3">
              <input
                className="custom-control-input"
                id={
                  "customCheckChapter" + item2.id_chapter + "Section" + item2.id
                }
                type="checkbox"
                onChange={handleChange}
                checked={item2.checked}
              />
              <label
                className="custom-control-label"
                htmlFor={
                  "customCheckChapter" + item2.id_chapter + "Section" + item2.id
                }
              >
                {item2.name}
              </label>
            </div>
          )}
        </Fragment>
      ))}
    </Fragment>
  ));

  return (
    <>
      <HeaderCustom />
      {hasquestion ? (
        <Row className="m-xl-4">
          <Col className="order-xl-2 mb-5 mb-xl-0" xl="8">
            <Card className="card-profile shadow">
              <Row className="justify-content-center"></Row>
              <CardHeader className="text-right border-0 pt-8 pt-md-4 pb-0 pb-md-4">
                <Button
                  className="btn-icon btn-2"
                  color="primary"
                  type="submit"
                  form="form-test"
                >
                  Submit
                </Button>
              </CardHeader>

              <CardBody className="pt-0 pt-md-4">
                <Form id="form-test" onSubmit={handleSubmitFormTest}>
                  <TabContent activeTab={"tabs" + tab}>
                    {question.map((item, index) => (
                      <TabPane tabId={"tabs" + (index + 1)} key={index}>
                        Question {index + 1}/{question.length}
                        <RawHTML className="description">
                          {item.content}
                        </RawHTML>
                        <p className="description">
                          Which of the following answers is correct?
                        </p>
                        <div className="custom-control custom-radio mb-3">
                          <input
                            className="custom-control-input"
                            id={"customRadioA" + index}
                            name={"question-radio-" + item.Question.id}
                            type="radio"
                            value="A"
                          />
                          <label
                            className="custom-control-label"
                            htmlFor={"customRadioA" + index}
                          >
                            A. {item.answer_a}
                          </label>
                        </div>
                        <div className="custom-control custom-radio mb-3">
                          <input
                            className="custom-control-input"
                            id={"customRadioB" + index}
                            name={"question-radio-" + item.Question.id}
                            type="radio"
                            value="B"
                          />
                          <label
                            className="custom-control-label"
                            htmlFor={"customRadioB" + index}
                          >
                            B. {item.answer_b}
                          </label>
                        </div>
                        <div className="custom-control custom-radio mb-3">
                          <input
                            className="custom-control-input"
                            id={"customRadioC" + index}
                            name={"question-radio-" + item.Question.id}
                            type="radio"
                            value="C"
                          />
                          <label
                            className="custom-control-label"
                            htmlFor={"customRadioC" + index}
                          >
                            C. {item.answer_c}
                          </label>
                        </div>
                        <div className="custom-control custom-radio mb-3">
                          <input
                            className="custom-control-input"
                            id={"customRadioD" + index}
                            name={"question-radio-" + item.Question.id}
                            type="radio"
                            value="D"
                          />
                          <label
                            className="custom-control-label"
                            htmlFor={"customRadioD" + index}
                          >
                            D. {item.answer_d}
                          </label>
                        </div>
                      </TabPane>
                    ))}
                  </TabContent>
                </Form>
              </CardBody>
            </Card>
          </Col>
          <Col className="order-xl-1" xl="4">
            <Card className="bg-secondary shadow">
              <CardHeader className="bg-white border-0">
                <Row className="align-items-center">
                  <Col xs="8">
                    <h3 className="mb-0">General</h3>
                  </Col>
                </Row>
              </CardHeader>
              <CardBody>
                <h6 className="heading-small text-muted mb-4">Duration</h6>
                <div className="pl-lg-4">
                  <Row>
                    <Col
                      lg="12"
                      className="d-flex justify-content-center align-content-center"
                    >
                      <div style={{ width: 150, height: 150 }}>
                        <CircularProgressbar
                          value={timeRemain}
                          maxValue={maxTime}
                          text={new Date(timeRemain * 1000)
                            .toISOString()
                            .substr(11, 8)}
                        />
                      </div>
                    </Col>
                  </Row>
                  <Row>
                    <Col lg="6"></Col>
                    <Col lg="6"></Col>
                  </Row>
                </div>
                <hr className="my-4" />
                {/* Address */}
                <h6 className="heading-small text-muted mb-4">Questions</h6>
                <div className="pl-lg-4">
                  <Row>
                    <Col md="12">
                      <Nav
                        className="nav-pills-circle flex-column flex-md-row"
                        id="tabs-icons-text"
                        pills
                        role="tablist"
                      >
                        {question.map((item, index) => (
                          <NavItem key={index}>
                            <NavLink
                              aria-selected={tab === index + 1}
                              className={classnames("mb-sm-3 mb-md-0", {
                                active: tab === index + 1,
                              })}
                              onClick={(e) => toggleNavs(e, "tabs", index + 1)}
                              href="#pablo"
                              role="tab"
                            >
                              <span className="nav-link-icon d-block">
                                {index + 1}
                              </span>
                            </NavLink>
                          </NavItem>
                        ))}
                      </Nav>
                    </Col>
                  </Row>
                </div>
                <hr className="my-4" />
                {/* Description */}
              </CardBody>
            </Card>
          </Col>
        </Row>
      ) : (
        <Card className="bg-secondary shadow  m-xl-4">
          <CardHeader className="bg-white border-0">
            <Row className="align-items-center">
              <Col xs="8">
                <h3 className="mb-0">Examination config</h3>
              </Col>
              <Col className="text-right" xs="4">
                <Button
                  color="primary"
                  href="#pablo"
                  onClick={(e) => e.preventDefault()}
                  size="sm"
                >
                  Settings
                </Button>
              </Col>
            </Row>
          </CardHeader>
          <CardBody>
            <Form role="form" onSubmit={handleSubmitForm}>
              <h6 className="heading-small text-muted mb-4">Exam content</h6>
              <div className="pl-lg-4">
                <Row>
                  <Col lg="6">
                    <FormGroup>
                      <label
                        className="form-control-label"
                        htmlFor="custom-radio"
                      >
                        Select chapter
                      </label>
                      {listChapter}
                    </FormGroup>
                  </Col>
                  <Col lg="6">
                    <FormGroup>
                      <label
                        className="form-control-label"
                        // htmlFor="custom-radio"
                      >
                        Time
                      </label>
                      <div
                        className="custom-control custom-radio mb-3"
                        id="custom-radio"
                      >
                        <input
                          className="custom-control-input"
                          id="customRadio5"
                          name="radio-time"
                          type="radio"
                          value={45}
                        />
                        <label
                          className="custom-control-label"
                          htmlFor="customRadio5"
                        >
                          45 Minutes
                        </label>
                      </div>
                      <div
                        className="custom-control custom-radio mb-3"
                        id="custom-radio1"
                      >
                        <input
                          className="custom-control-input"
                          id="customRadio6"
                          name="radio-time"
                          type="radio"
                          value={60}
                          required
                        />
                        <label
                          className="custom-control-label"
                          htmlFor="customRadio6"
                        >
                          60 Minutes
                        </label>
                      </div>
                    </FormGroup>
                  </Col>
                </Row>
                <Row>
                  <Col log="12" className="d-flex column">
                    <Button
                      className="align-self-end"
                      color="primary"
                      type="submit"
                    >
                      Start
                    </Button>
                  </Col>
                </Row>
              </div>
            </Form>

            <Modal
              fade={false}
              centered
              isOpen={loading}
              toggle={function noRefCheck() {}}
            >
              <ModalBody
                className="d-flex justify-content-center align-content-center"
                style={{ height: "300px" }}
              >
                <Loader />
              </ModalBody>
            </Modal>
          </CardBody>
        </Card>
      )}
    </>
  );
};

export default Testing;
