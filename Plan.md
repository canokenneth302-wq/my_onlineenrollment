# Plan: Hello World page (HTML)

## Build command

<!-- Điền / chạy build command tại đây. Chưa có build command thì chưa viết code. -->

## Yêu cầu

- Init trang hello world bằng HTML.
- Chạy script `console.log("Hello world")`.

## Phase 1: Trang HTML

- Tạo `index.html` ở root repo (HTML5, `lang="vi"`, `charset` UTF-8, viewport).
- Nội dung: `<h1>Hello world</h1>`.
- Nạp script bằng `<script src="script.js" defer></script>`.

## Phase 2: Script

- Tạo `script.js` ở root repo, chỉ chứa `console.log("Hello world");`.

## Phase 3: Kiểm tra

- Mở `index.html` trong trình duyệt, xem Console có dòng `Hello world`.
- Hoặc chạy `bun script.js` để kiểm tra nhanh log ở terminal.

## Câu hỏi mở

1. Để script trong file riêng `script.js` (đề xuất) hay viết inline trong `index.html`?
2. Có cần dev server (ví dụ `bunx serve`), hay mở file trực tiếp là đủ?
