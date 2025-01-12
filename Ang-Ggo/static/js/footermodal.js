// 6. 모달창 클릭
document.addEventListener("DOMContentLoaded", () => {
  const emailModal = document.querySelector('#emailModal'); // 이메일 모달 참조
  const clauseModal = document.querySelector('#clauseModal'); // 이용약관 모달 참조
  const btnOpenEmailModal = document.querySelector('#no_email'); // 이메일 무단 수집 버튼 참조
  const btnOpenClauseModal = document.querySelector('#clause'); // 이용약관 버튼 참조
  const btnCloseEmailModal = document.querySelector('#closeBtn'); // 이메일 모달 닫기 버튼 참조
  const btnCloseClauseModal = document.querySelector('#closeClauseBtn'); // 이용약관 모달 닫기 버튼 참조

  // 이메일 무단 수집 모달 열기
  btnOpenEmailModal.addEventListener("click", (e) => {
      e.preventDefault(); // 기본 링크 동작 방지
      emailModal.style.display = "flex"; // 모달 보이기
      document.body.classList.add("modal-open"); // 모달 오픈 클래스 추가
  });

  // 이용약관 모달 열기
  btnOpenClauseModal.addEventListener("click", (e) => {
      e.preventDefault(); // 기본 링크 동작 방지
      clauseModal.style.display = "flex"; // 모달 보이기
      document.body.classList.add("modal-open"); // 모달 오픈 클래스 추가
  });

  // 이메일 모달 닫기
  btnCloseEmailModal.addEventListener("click", () => {
      emailModal.style.display = "none"; // 이메일 모달 숨기기
      document.body.classList.remove("modal-open"); // 모달 오픈 클래스 제거
  });

  // 이용약관 모달 닫기
  btnCloseClauseModal.addEventListener("click", () => {
      clauseModal.style.display = "none"; // 이용약관 모달 숨기기
      document.body.classList.remove("modal-open"); // 모달 오픈 클래스 제거
  });
});