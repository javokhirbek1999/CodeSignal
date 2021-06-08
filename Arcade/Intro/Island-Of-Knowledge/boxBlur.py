def boxBlur(image):
    def square_matrix(square):
        total_sum = 0
        for i in range(3):
            for j in range(3):
                total_sum += square[i][j]
        
        return total_sum//9
    
    square = []

    square_row = []

    blur_row = []

    blur_img = []

    n_rows = len(image)

    n_cols = len(image[0])

    row_p,col_p = 0,0

    while row_p <= n_rows-3:
        while col_p <= n_cols-3:
            for i in range(row_p,row_p+3):
                for j in range(col_p,col_p+3):
                    square_row.append(image[i][j])
                
                square.append(square_row)
                square_row = []

            blur_row.append(square_matrix(square))
            square = []

            col_p += 1
        
        blur_img.append(blur_row)
        blur_row = []
        row_p += 1
        col_p = 0
    return blur_img
