import tag



a = [[155, 58, 14, 116, 154],
[189, 28, 164, 111, 98],
[134, 154, 84, 88, 74],
[181, 199, 14, 116, 114],
[94, 28, 109, 86, 183],
[61, 199, 91, 128, 108],
[156, 173, 178, 84, 69],
[22, 88, 62, 79, 112],
[16, 198, 143, 113, 19],
[101, 139, 177, 197, 19],
[164, 25, 142, 50, 172],
[68, 39, 167, 184, 148],
[132, 176, 1, 104, 67],
[154, 147, 190, 102, 155],
[133, 107, 185, 139, 97],
[165, 12, 133, 199, 197],
[15, 147, 73, 131, 83],
[155, 154, 151, 160, 97],
[182, 116, 155, 154, 62],
[114, 134, 17, 62, 64],
[67, 9, 44, 166, 83],
[22, 129, 56, 144, 24],
[50, 63, 142, 148, 100],
[166, 127, 118, 60, 190],
[15, 141, 69, 83, 171],
[146, 102, 89, 190, 195],
[169, 147, 100, 146, 68],
[73, 149, 142, 67, 166],
[42, 183, 59, 170, 135],
[102, 36, 17, 180, 42]]


b = [
[124, 136, 112, 186, 106],
[189, 28, 164, 111, 98],
[134, 154, 79, 186, 106],
[181, 199, 14, 116, 114],
[94, 28, 86, 183, 42],
[61, 91, 108, 184, 175],
[156, 65, 999, 155, 116],
[22, 62, 79, 154, 73],
[153, 176, 126, 21, 145],
[177, 19, 141, 169, 157],
[48, 172, 25, 142, 164],
[39, 167, 184, 148, 136],
[132, 1, 104, 67, 34],
[154, 147, 190, 102, 155],
[133, 107, 139, 97, 64],
[12, 133, 199, 197, 53],
[15, 147, 73, 131, 83],
[154, 160, 97, 118, 155],
[168, 134, 116, 14, 154],
[64, 62, 127, 88, 37],
[142, 166, 83, 15, 73],
[122, 143, 24, 19, 22],
[64, 53, 111, 188, 172],
[60, 132, 99, 129, 23],
[69, 83, 171, 15, 141],
[146, 102, 190, 195, 189],
[147, 169, 100, 146, 68],
[149, 142, 67, 166, 83],
[111, 183, 117, 69, 70],
[36, 17, 180, 42, 65]]


c = [
[124, 136, 112, 186, 106],
[189, 28, 164, 111, 75],
[154, 88, 79, 106, 173],
[199, 14, 114, 62, 22],
[94, 28, 183, 42, 117],
[61, 91, 184, 175, 98],
[65, 999, 116, 178, 173],
[22, 62, 79, 154, 14],
[16, 55, 40, 23, 167],
[101, 177, 19, 164, 137],
[172, 142, 164, 113, 48],
[39, 167, 184, 148, 136],
[104, 67, 34, 174, 145],
[154, 147, 190, 102, 155],
[133, 185, 118, 26, 153],
[165, 55, 76, 62, 178],
[15, 73, 131, 176, 132],
[129, 118, 160, 97, 155],
[168, 134, 116, 154, 88],
[134, 64, 62, 127, 88],
[142, 166, 83, 15, 73],
[22, 56, 144, 24, 143],
[999, 6, 32, 91, 61],
[166, 127, 90, 22, 138],
[69, 83, 193, 171, 15],
[146, 102, 190, 195, 189],
[147, 169, 146, 178, 195],
[142, 67, 166, 83, 15],
[170, 135, 117, 14, 82],
[102, 36, 17, 180, 42]]



d = [
[124, 116, 88, 127, 136],
[31, 152, 7, 28, 50],
[116, 127, 168, 182, 88],
[64, 127, 168, 182, 14],
[3, 94, 109, 192, 8],
[185, 98, 6, 29, 53],
[69, 16, 65, 178, 0],
[127, 168, 182, 116, 88],
[13, 101, 11, 12, 32],
[32, 153, 130, 68, 184],
[95, 167, 25, 46, 48],
[177, 57, 151, 32, 153],
[100, 132, 172, 50, 57],
[194, 195, 81, 120, 190],
[22, 34, 97, 107, 115],
[29, 128, 137, 175, 199],
[44, 88, 9, 67, 73],
[118, 78, 191, 106, 160],
[58, 116, 88, 127, 136],
[127, 168, 182, 116, 88],
[44, 88, 9, 67, 73],
[22, 65, 122, 144, 19],
[139, 57, 161, 174, 108],
[129, 99, 90, 120, 190],
[141, 15, 20, 41, 51],
[81, 120, 190, 194, 89],
[78, 5, 68, 96, 97],
[74, 105, 149, 44, 88],
[1, 141, 14, 79, 84],
[102, 34, 65, 140, 172]]

# [124, 116, 88, 127, 136, 168, 182, 0, 14, 37]
# [31, 152, 7, 28, 50, 57, 63, 67, 75, 87]
# [116, 127, 168, 182, 88, 136, 14, 37, 79, 99]
# [64, 127, 168, 182, 14, 191, 199, 34, 71, 104]
# [3, 94, 109, 192, 8, 110, 114, 7, 18, 21]
# [185, 98, 6, 29, 53, 61, 38, 91, 0, 5]
# [69, 16, 65, 178, 0, 14, 37, 58, 62, 74]
# [127, 168, 182, 116, 88, 136, 14, 37, 79, 99]
# [13, 101, 11, 12, 32, 66, 153, 198, 56, 196]
# [32, 153, 130, 68, 184, 12, 11, 66, 198, 13]
# [95, 167, 25, 46, 48, 73, 113, 161, 50, 57]
# [177, 57, 151, 32, 153, 130, 68, 184, 11, 12]
# [100, 132, 172, 50, 57, 63, 67, 111, 142, 164]
# [194, 195, 81, 120, 190, 89, 27, 146, 147, 176]
# [22, 34, 97, 107, 115, 118, 129, 151, 0, 5]
# [29, 128, 137, 175, 199, 113, 16, 62, 0, 5]
# [44, 88, 9, 67, 73, 142, 15, 45, 51, 83]
# [118, 78, 191, 106, 160, 97, 129, 151, 146, 154]
# [58, 116, 88, 127, 136, 168, 182, 0, 14, 37]
# [127, 168, 182, 116, 88, 136, 14, 37, 79, 99]
# [44, 88, 9, 67, 73, 142, 15, 45, 51, 83]
# [22, 65, 122, 144, 19, 24, 56, 123, 129, 143]
# [139, 57, 161, 174, 108, 197, 91, 60, 106, 86]
# [129, 99, 90, 120, 190, 97, 118, 151, 6, 14]
# [141, 15, 20, 41, 51, 83, 131, 171, 193, 69]
# [81, 120, 190, 194, 89, 27, 146, 147, 176, 195]
# [78, 5, 68, 96, 97, 100, 169, 178, 187, 188]
# [74, 105, 149, 44, 88, 9, 67, 73, 142, 15]
# [1, 141, 14, 79, 84, 98, 4, 28, 31, 42]
# [102, 34, 65, 140, 172, 174, 2, 17, 36, 42]










e=[
[114, 112, 74, 138, 79],
[152, 172, 183, 164, 140],
[60, 116, 73, 134, 182],
[199, 22, 182, 138, 191],
[94, 109, 145, 183, 162],
[38, 139, 76, 128, 137],
[79, 65, 114, 155, 58],
[106, 79, 138, 22, 14],
[127, 143, 24, 101, 113],
[199, 105, 53, 113, 76],
[48, 176, 25, 63, 172],
[57, 151, 13, 39, 167],
[100, 132, 1, 5, 111],
[27, 120, 195, 189, 194],
[60, 185, 128, 133, 61],
[165, 178, 130, 53, 113],
[147, 15, 131, 132, 176],
[187, 154, 151, 97, 160],
[168, 84, 134, 114, 173],
[134, 58, 182, 60, 127],
[83, 15, 88, 142, 9],
[144, 56, 19, 143, 24],
[50, 63, 29, 999, 68],
[127, 60, 181, 114, 197],
[15, 193, 41, 20, 69],
[156, 102, 132, 154, 89],
[162, 80, 26, 146, 5],
[88, 51, 67, 45, 166],
[170, 183, 82, 69, 152],
[102, 72, 100, 17, 65]]

f = [
[58, 14, 99, 106, 116],
[152, 172, 183, 164, 31],
[127, 116, 73, 22, 999],
[199, 22, 79, 156, 191],
[94, 109, 145, 162, 177],
[76, 128, 165, 178, 55],
[79, 114, 155, 58, 69],
[106, 79, 138, 22, 112],
[55, 126, 143, 164, 71],
[199, 105, 113, 53, 177],
[161, 95, 67, 63, 172],
[57, 13, 151, 39, 167],
[100, 1, 5, 111, 63],
[27, 120, 195, 189, 194],
[53, 199, 139, 128, 169],
[16, 133, 184, 137, 100],
[176, 83, 9, 27, 120],
[187, 154, 129, 151, 97],
[127, 173, 88, 186, 999],
[116, 58, 182, 60, 73],
[83, 15, 142, 9, 166],
[56, 19, 143, 24, 122],
[50, 999, 68, 142, 5],
[127, 60, 181, 114, 22],
[141, 51, 20, 104, 69],
[102, 10, 176, 132, 27],
[162, 169, 25, 68, 97],
[51, 142, 67, 45, 166],
[82, 69, 96, 1, 152],
[102, 72, 100, 17, 181]
]

g = [
[58, 99, 106, 134, 182],
[152, 172, 183, 164, 111],
[116, 22, 999, 173, 168],
[17, 71, 154, 64, 134],
[94, 109, 145, 162, 18],
[76, 128, 184, 165, 178],
[106, 114, 155, 58, 69],
[106, 79, 22, 112, 14],
[24, 101, 113, 40, 32],
[199, 105, 113, 177, 40],
[161, 95, 142, 63, 172],
[13, 56, 167, 184, 71],
[1, 5, 63, 174, 145],
[102, 195, 189, 194, 155],
[53, 128, 169, 184, 175],
[133, 184, 137, 100, 165],
[190, 176, 83, 9, 27],
[187, 154, 151, 160, 97],
[58, 114, 14, 112, 74],
[116, 6, 54, 173, 168],
[142, 9, 166, 83, 73],
[56, 19, 143, 24, 122],
[50, 29, 175, 106, 184],
[166, 182, 60, 114, 190],
[141, 20, 69, 83, 171],
[146, 156, 176, 154, 147],
[147, 162, 169, 146, 5],
[51, 142, 67, 45, 166],
[82, 69, 152, 84, 28],
[65, 172, 166, 174, 55]]

h = [
[114, 154, 124, 88, 74],
[189, 164, 135, 87, 176],
[60, 134, 73, 64, 132],
[199, 197, 73, 184, 22],
[145, 28, 183, 86, 42],
[12, 178, 61, 133, 185],
[62, 74, 138, 106, 65],
[79, 23, 136, 22, 6],
[12, 127, 143, 164, 24],
[11, 113, 197, 53, 105],
[73, 46, 176, 95, 67],
[27, 196, 13, 68, 56],
[100, 137, 132, 34, 50],
[147, 120, 195, 189, 194],
[199, 60, 53, 64, 169],
[165, 55, 133, 188, 139],
[73, 27, 166, 195, 83],
[155, 187, 146, 191, 151],
[168, 134, 58, 197, 14],
[116, 134, 60, 73, 155],
[166, 73, 51, 83, 15],
[123, 65, 143, 24, 122],
[50, 999, 5, 142, 191],
[118, 73, 197, 190, 17],
[41, 69, 83, 171, 15],
[102, 176, 132, 89, 190],
[162, 147, 96, 178, 97],
[15, 51, 142, 45, 166],
[82, 149, 152, 134, 47],
[100, 72, 85, 17, 2]]

r=[
[124, 99, 182, 999, 173],
[164, 87, 63, 57, 28],
[134, 73, 132, 74, 184],
[73, 197, 184, 22, 106],
[145, 183, 86, 42, 162],
[12, 61, 178, 199, 53],
[65, 58, 69, 84, 173],
[79, 23, 136, 22, 6],
[127, 113, 19, 85, 176],
[11, 53, 105, 76, 188],
[95, 67, 172, 164, 113],
[151, 66, 39, 74, 40],
[100, 137, 132, 188, 118],
[154, 147, 120, 195, 189],
[199, 60, 53, 64, 169],
[165, 55, 133, 188, 76],
[166, 195, 83, 189, 194],
[155, 187, 191, 151, 160],
[134, 58, 74, 62, 173],
[60, 114, 182, 84, 166],
[166, 73, 67, 83, 15],
[65, 143, 24, 122, 19],
[29, 63, 68, 6, 175],
[73, 197, 190, 17, 64],
[171, 15, 18, 20, 69],
[176, 132, 89, 190, 27],
[147, 96, 178, 97, 195],
[105, 9, 45, 166, 83],
[149, 152, 134, 47, 84],
[72, 85, 17, 2, 181]]

t = [
[124, 182, 999, 173, 127],
[164, 87, 63, 57, 28],
[60, 134, 73, 74, 106],
[73, 197, 184, 22, 106],
[145, 86, 114, 177, 59],
[12, 61, 53, 153, 5],
[99, 156, 106, 37, 116],
[79, 6, 999, 155, 116],
[127, 113, 19, 176, 142],
[11, 53, 105, 76, 188],
[48, 164, 46, 176, 167],
[151, 66, 39, 74, 40],
[100, 176, 132, 50, 188],
[120, 195, 189, 194, 155],
[199, 53, 64, 169, 22],
[165, 55, 188, 64, 199],
[166, 195, 189, 83, 194],
[155, 187, 160, 97, 118],
[134, 58, 62, 173, 127],
[60, 182, 84, 166, 14],
[67, 44, 166, 83, 73],
[65, 143, 24, 122, 19],
[29, 63, 6, 175, 77],
[97, 60, 181, 17, 14],
[171, 15, 131, 18, 20],
[176, 132, 89, 27, 189],
[147, 96, 178, 97, 195],
[105, 166, 83, 73, 15],
[152, 134, 47, 84, 28],
[72, 85, 17, 2, 185]]
p1=[
[134, 84, 79, 58, 0],
[31, 142, 87, 7, 50],
[166, 0, 127, 62, 17],
[34, 184, 182, 155, 54],
[4, 41, 177, 192, 110],
[169, 98, 128, 184, 130],
[84, 134, 114, 16, 112],
[73, 99, 37, 54, 181],
[157, 21, 105, 127, 196],
[16, 177, 145, 76, 105],
[46, 50, 161, 111, 95],
[12, 198, 148, 27, 164],
[137, 20, 169, 174, 50],
[147, 154, 155, 146, 190],
[106, 188, 191, 12, 185],
[153, 61, 169, 100, 113],
[88, 67, 146, 166, 131],
[154, 146, 97, 160, 118],
[136, 37, 114, 116, 197],
[62, 173, 134, 182, 136],
[83, 45, 166, 131, 15],
[122, 24, 56, 144, 123],
[100, 142, 197, 61, 169],
[22, 23, 106, 186, 127],
[41, 193, 131, 141, 171],
[195, 132, 154, 81, 146],
[78, 187, 80, 26, 9],
[142, 83, 88, 73, 67],
[183, 134, 141, 59, 150],
[172, 133, 52, 42, 85]]

p2=[
[186, 182, 124, 0, 127],
[176, 50, 98, 111, 183],
[54, 156, 114, 37, 60],
[184, 199, 134, 182, 106],
[94, 4, 8, 18, 86],
[128, 29, 106, 60, 91],
[62, 112, 178, 0, 134],
[73, 114, 156, 182, 64],
[23, 35, 39, 141, 153],
[196, 5, 169, 165, 141],
[161, 50, 167, 95, 111],
[126, 164, 177, 57, 40],
[130, 176, 104, 137, 174],
[89, 176, 102, 189, 10],
[118, 178, 34, 22, 0],
[199, 26, 0, 153, 175],
[132, 45, 166, 146, 131],
[191, 154, 146, 97, 160],
[112, 186, 106, 88, 138],
[166, 173, 182, 112, 106],
[83, 166, 45, 131, 88],
[56, 65, 122, 144, 123],
[176, 91, 68, 199, 29],
[22, 6, 182, 17, 166],
[131, 141, 171, 41, 193],
[189, 155, 147, 10, 146],
[78, 30, 54, 5, 179],
[166, 131, 74, 83, 88],
[134, 98, 50, 111, 183],
[102, 140, 181, 55, 174]]

p3=[
[134, 114, 156, 37, 154],
[140, 142, 7, 50, 98],
[62, 60, 106, 155, 73],
[199, 134, 156, 191, 138],
[41, 111, 192, 110, 183],
[178, 100, 0, 175, 128],
[156, 178, 16, 154, 138],
[154, 23, 116, 132, 168],
[104, 157, 23, 113, 177],
[196, 85, 169, 56, 128],
[172, 48, 95, 161, 50],
[184, 130, 71, 85, 127],
[67, 142, 111, 169, 174],
[195, 146, 190, 189, 102],
[199, 153, 0, 175, 128],
[12, 188, 16, 106, 133],
[166, 146, 131, 190, 195],
[154, 146, 97, 160, 191],
[136, 156, 74, 116, 173],
[114, 136, 156, 155, 88],
[166, 131, 88, 15, 83],
[122, 143, 56, 144, 123],
[164, 26, 178, 199, 29],
[14, 64, 73, 151, 138],
[83, 69, 193, 131, 141],
[156, 27, 146, 190, 195],
[78, 100, 179, 146, 169],
[105, 166, 131, 74, 88],
[183, 50, 98, 111, 70],
[172, 180, 121, 174, 166]]


result = 0
for i in range(len(a)):
	for j in range(len(a[i])):
		if p3[i][j] in d[i]:
			result = result+1
print(result)
# 
# 
# 
# 