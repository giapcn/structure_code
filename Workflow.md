# Git Workflow

Mô tả Workflow làm việc của team khi triển khai dự án

## Table of Contents

- [Git Workflow](#git-workflow)
  - [Table of Contents](#table-of-contents)
  - [1. Branch structure (Branching Strategy)](#1-branch-structure-branching-strategy)
  - [2. Workflow](#2-workflow)
    - [Quy trình tạo và phát triển nhánh tính năng:](#quy-trình-tạo-và-phát-triển-nhánh-tính-năng)
    - [Quy trình tạo và phát triển nhánh thử nghiệm:](#quy-trình-tạo-và-phát-triển-nhánh-thử-nghiệm)
    - [Quy trình sửa lỗi khẩn cấp:](#quy-trình-sửa-lỗi-khẩn-cấp)
  - [3. Quy tắc Commit và Pull Request](#3-quy-tắc-commit-và-pull-request)
    - [Quy tắc Commit:](#quy-tắc-commit)
    - [Quy tắc Pull Request:](#quy-tắc-pull-request)
    - [Tóm Tắt Các Bước:](#tóm-tắt-các-bước)

## 1. Branch structure (Branching Strategy)

**Các loại nhánh cơ bản:**

1. Main (hoặc master): Nhánh chính, chứa mã nguồn ổn định nhất (base code).
2. Develop: Nhánh phát triển, nơi tích hợp tất cả các thay đổi từ các nhánh tính năng.
3. Feature Branches: Nhánh tính năng, tạo cho mỗi bài học hoặc chủ đề cụ thể.
4. Experiment Branches: Nhánh thử nghiệm, dùng cho các thử nghiệm hoặc nghiên cứu các khái niệm mới.
5. Deploy: Nhánh triển khai.
6. Bugfix/Hotfix Branches: Nhánh sửa lỗi, dùng để sửa các lỗi phát hiện trong nhánh phát triển hoặc triển khai.

## 2. Workflow

### Quy trình tạo và phát triển nhánh tính năng:

**1. Tạo nhánh tính năng từ nhánh phát triển:**

```bash
git checkout develop
git checkout -b feature/feature_name
```

**2. Phát triển tính năng hoặc thực hiện bài học trên nhánh tính năng.**

**3. Commit và đẩy nhánh lên repository:**

```bash
git add .
git commit -m "Mô tả thay đổi"
git push origin feature/feature_name
```

**4. Tạo Pull Request (PR):**

- Mở pull request từ nhánh tính năng đến nhánh develop.
- Mô tả chi tiết về thay đổi và khái niệm đã học trong PR.

**5. Kiểm tra mã (Code Review):**

- Các thành viên khác xem xét và đưa ra phản hồi trên PR.
- Thảo luận và chỉnh sửa mã dựa trên phản hồi.

**6. Hợp nhất nhánh tính năng vào nhánh phát triển:**

Sau khi PR được chấp thuận, hợp nhất (merge) vào nhánh develop.

```bash
git checkout develop
git merge feature/feature_name
```

### Quy trình tạo và phát triển nhánh thử nghiệm:

**1. Tạo nhánh thử nghiệm từ nhánh phát triển:**

```sh
git checkout develop
git checkout -b experiment/experiment_name
```

**2. Thực hiện thử nghiệm và commit.**

**3. Đẩy nhánh thử nghiệm lên repository:**

```sh
git push origin experiment/experiment_name
```

**4. Tạo Pull Request (PR):**

- Tạo PR từ nhánh thử nghiệm đến nhánh develop.
- Mô tả chi tiết về thử nghiệm và kết quả.

**5. Kiểm tra mã (Code Review) và hợp nhất tương tự như nhánh tính năng.**

### Quy trình sửa lỗi khẩn cấp:

**1. Tạo nhánh sửa lỗi từ nhánh chính:**

```sh
git checkout deploy
git checkout -b hotfix/bug_[bug_name]
```

## 3. Quy tắc Commit và Pull Request

### Quy tắc Commit:

**Thông điệp commit rõ ràng và có ý nghĩa:**

```sh
git commit -m "OOP: Thêm ví dụ về kế thừa và đa hình"
```

**Commit nhỏ và dễ quản lý:**

- Mỗi commit nên tập trung vào một khía cạnh cụ thể của bài học hoặc tính năng.

### Quy tắc Pull Request:

**Mô tả chi tiết:**

- Mô tả bài học hoặc khái niệm OOP, mẫu thiết kế hoặc cơ sở dữ liệu mà pull request đang áp dụng.
- Đưa ra các câu hỏi hoặc điểm cần thảo luận.

**Kiểm tra và phản hồi:**

- Các thành viên trong nhóm nên kiểm tra mã nguồn, đưa ra phản hồi và thảo luận về các khái niệm hoặc mẫu thiết kế.

### Tóm Tắt Các Bước:

- `Tạo Issue`: Mô tả tính năng hoặc vấn đề.
- `Tạo nhánh feature`: Phát triển và đẩy lên.
- `Tạo PR từ feature đến develop`: Code review và hợp nhất.
- `Tạo nhánh experiment`: Thử nghiệm và đẩy lên.
- `Tạo PR từ experiment đến develop`: Code review và hợp nhất.
- `Merge develop vào deploy`: Triển khai thực tế.
