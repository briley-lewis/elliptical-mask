from imgmasks import ellipse

#will need to keep axis ratio constant
def bn(an,a,b):
    bn = (b*an)/a
    return bn

def make_annulus(center,a1,b1,imgsize,step,theta=0):
    outer = ellipse.Ellipse(center,a1,b1,imgsize,theta=theta)
    mask1 = outer.make_ellipse()
    mask1[mask1==0] = np.nan
    
    if a1==b1:
        b2=a2
    else:
        a2 = a1-step
        b2 = bn(a2,a1,b1)
    
    inner = ellipse.Ellipse(center,a2,b2,[281,281],theta=12)
    mask2 = inner.make_ellipse()
    mask2[mask2==1] = np.nan
    mask2[mask2==0] = 1
    
    mask = mask1+mask2
    mask[np.isnan(mask)]=0
    return mask
